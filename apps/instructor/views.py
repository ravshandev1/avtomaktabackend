from django.shortcuts import get_object_or_404
from rest_framework import generics, response, views
from .models import Instructor, Tuman, Rating
from .serializers import InstructorSerializer, TumanSerializer
from session.serializers import MoshinaSerializer
from session.models import Car, Session
from client.models import Client


class FreeTimeAPI(views.APIView):
    def get(self, request, *args, **kwargs):
        telegram_id = self.request.query_params.get('tel_id')
        date = self.request.query_params.get('date')
        dt = date.split('-')
        day = dt[2]
        month = dt[1]
        year = dt[0]
        sessions = Session.objects.filter(instructor__telegram_id=telegram_id, vaqt__day=day, vaqt__year=year,
                                          vaqt__month=month, is_finished=False).all()
        data = dict()
        if sessions:
            data['vaqt'] = [f"{str(item.vaqt)[11:16]}" for item in sessions]
        else:
            data['vaqt'] = 'Band qilinmagan!'
        return response.Response(data)


class IncreaseBalanceAPI(views.APIView):
    def post(self, request, *args, **kwargs):
        summa = int(self.request.data['summa'])
        instructor = int(self.request.data['instructor'])
        obj = Instructor.objects.filter(telegram_id=instructor).first()
        obj.balans += (summa // 100)
        obj.save()
        return response.Response({'message': "Балансингиз тўлдирилди!!!"})


class RatingAPI(views.APIView):
    def post(self, request, *args, **kwargs):
        client = int(self.request.data['client'])
        instructor = int(self.request.data['instructor'])
        i_id = Instructor.objects.filter(telegram_id=instructor).first()
        c_id = Client.objects.filter(telegram_id=client).first()
        Rating.objects.create(instructor_id=i_id.id, client_id=c_id.id)
        return response.Response({'message': "Бахолаш учун рахмат!!!"})

    def patch(self, request, *args, **kwargs):
        client = int(self.request.data['client'])
        rate = int(self.request.data['rate'])
        rt = Rating.objects.filter(client__telegram_id=client).all()
        rs = rt.filter(rate=0).first()
        rs.rate = rate
        rs.save()
        return response.Response({'message': "Бахолаш учун рахмат!!!"})


class RegionListAPI(generics.ListAPIView):
    queryset = Tuman.objects.all()
    serializer_class = TumanSerializer


class CarListAPI(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = MoshinaSerializer

    def get_queryset(self):
        cat = self.request.query_params.get('cat')
        if cat:
            return self.queryset.filter(categoriyasi__toifa=cat).all()
        return self.queryset.all()


class InstructorAPI(generics.CreateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tel = serializer.validated_data['telegram_id']
        if Instructor.objects.filter(telegram_id=tel).first():
            return response.Response({'message': "ботимиздан аввал рўйхатдан ўтгансиз!"})
        serializer.save()
        return response.Response({'message': "ботимиздан рўйхатдан ўтдингиз!"})

    def get(self, request, *args, **kwargs):
        qs = self.queryset.filter(telegram_id=self.kwargs['pk'])
        serializer = self.get_serializer(instance=get_object_or_404(qs))
        return response.Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        qs = self.queryset.filter(telegram_id=self.kwargs['pk'])
        serializer = self.get_serializer(instance=get_object_or_404(qs), data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)
