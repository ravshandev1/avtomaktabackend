from rest_framework import generics, response, views, status
from .models import Session, Car, Price, Percent, TextSes
from .serializers import SessionSerializer, CategorySerializer, SessionListSerializer, PriceSerializer, \
    PercentSerializer, TextSerializer
from instructor.serializers import InstructorSerializer
from instructor.models import Instructor
from client.models import Client, Category
from .paginations import CustomPagination
from django.db.models import Q


class TextAPI(generics.RetrieveAPIView):
    queryset = TextSes.objects.all()
    serializer_class = TextSerializer


class PercentAPI(generics.ListAPIView):
    queryset = Percent.objects.all()
    serializer_class = PercentSerializer


class PriceListAPI(generics.ListAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

    def get_queryset(self):
        qs = self.queryset.filter(category__instructors__balans__isnull=False)
        return qs.order_by('category').distinct('category')


class PriceAPI(generics.ListAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

    def get(self, request, *args, **kwargs):
        s_id = self.request.query_params.get('s_id')
        obj = Session.objects.filter(id=s_id).first()
        cat = obj.toifa
        queryset = self.queryset.filter(category__toifa__exact=cat).first()
        serializer = self.get_serializer(queryset)
        return response.Response(serializer.data)


class CategoryAPI(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class FilterCreateAPI(generics.ListAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

    def get_queryset(self):
        qs = self.queryset.order_by('tuman').distinct('tuman')
        tum = self.request.query_params.get('tum')
        if tum:
            qs = self.queryset.filter(tuman__exact=tum).order_by('toifa').distinct('toifa')
        cat = self.request.query_params.get('cat')
        if cat:
            qs = self.queryset.filter(Q(tuman__exact=tum), Q(toifa__toifa__exact=cat)).order_by('jins').distinct('jins')
        gen = self.request.query_params.get('gen')
        if gen:
            qs = self.queryset.filter(Q(tuman__exact=tum), Q(toifa__toifa__exact=cat), Q(jins=gen)).order_by(
                'moshina').distinct('moshina')
        car = self.request.query_params.get('car')
        if car:
            qs = self.queryset.filter(Q(tuman__exact=tum), Q(toifa__toifa__exact=cat), Q(jins__exact=gen),
                                      Q(moshina__exact=car))
        return qs

    def post(self, request, *args, **kwargs):
        ins_tg = self.request.data['ins_tg_id']
        car_name = self.request.data['moshina']
        tg_id = self.request.data['telegram_id']
        cat = self.request.data['toifa']
        car = Car.objects.filter(nomi=car_name).first()
        instructor = Instructor.objects.filter(telegram_id=ins_tg).first()
        client = Client.objects.filter(telegram_id=tg_id).first()

        data = dict()
        data['client'] = client.id
        data['instructor'] = instructor.id
        data['moshina'] = car.id
        data['toifa'] = self.request.data['toifa']
        data['jins'] = self.request.data['jins']
        data['tulov_turi'] = self.request.data['tulov_turi']
        data['vaqt'] = self.request.data['vaqt']
        serializer = SessionSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)


class UserFilterAPI(views.APIView):
    def get_queryset(self):
        tg_id = self.request.query_params.get('id')
        cl = Client.objects.filter(telegram_id=tg_id).first()
        ins = Instructor.objects.filter(telegram_id=tg_id).filter()
        if cl:
            return "Client"
        elif ins:
            return "Instructor"
        else:
            return "Not registered"

    def get(self, request, *args, **kwargs):
        return response.Response({'message': self.get_queryset()})


class SessionListAPI(generics.ListAPIView):
    queryset = Session.objects.filter(is_finished=False).all()
    pagination_class = CustomPagination

    def get_queryset(self):
        cl = Client.objects.filter(telegram_id=self.kwargs['pk']).first()
        ins = Instructor.objects.filter(telegram_id=self.kwargs['pk']).first()
        if cl:
            return self.queryset.filter(client=cl).all()
        elif ins:
            return self.queryset.filter(instructor=ins).all()

    def get_serializer_class(self):
        return SessionListSerializer


class IsFinishedSessions(generics.ListAPIView):
    queryset = Session.objects.filter(is_finished=True).all()
    pagination_class = CustomPagination

    def get_queryset(self):
        cl = Client.objects.filter(telegram_id=self.kwargs['pk']).first()
        ins = Instructor.objects.filter(telegram_id=self.kwargs['pk']).first()
        if cl:
            return self.queryset.filter(client=cl).all()
        elif ins:
            return self.queryset.filter(instructor=ins).all()

    def get_serializer_class(self):
        return SessionListSerializer


class SessionDetail(generics.RetrieveUpdateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    def patch(self, request, *args, **kwargs):
        obj = self.queryset.filter(id=kwargs['pk']).first()
        obj.is_finished = True
        obj.save()
        ins = self.request.query_params.get('ins')
        inst = Instructor.objects.filter(telegram_id=ins).first()
        # summa = int(self.request.data['summa'])
        # per = Percent.objects.filter(id=1).first()
        # inst.balans -= (summa * per.percent) / 100
        # inst.save()
        return response.Response({'client': obj.client.telegram_id, 'balance': inst.balans})

    def delete(self, request, *args, **kwargs):
        obj = self.queryset.filter(id=kwargs['pk']).first()
        obj.delete()
        return response.Response({'vaqt': obj.vaqt.__format__('%-d.%m.%Y %H:%M'), 'id': obj.instructor.telegram_id}, status=status.HTTP_200_OK)


class SessionLocationAPI(views.APIView):
    def get(self, request, *args, **kwargs):
        obj = Session.objects.filter(id=self.kwargs['pk']).first()
        loc = obj.instructor.location
        ls = loc.split(', ')
        return response.Response({'lat': ls[0], 'lon': ls[1]})
