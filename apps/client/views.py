from rest_framework import generics, response, status, views
from .models import Client, TextClientRegister, TextClientUpdate
from .serializers import ClientSerializer, TextRSerializer, TextUSerializer
from django.shortcuts import get_object_or_404
from instructor.models import Instructor


class TextRAPI(generics.RetrieveAPIView):
    queryset = TextClientRegister
    serializer_class = TextRSerializer


class TextUAPI(generics.RetrieveAPIView):
    queryset = TextClientUpdate
    serializer_class = TextUSerializer


class ClientAPI(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tel = serializer.validated_data['telegram_id']
        if Client.objects.filter(telegram_id=tel).first():
            return response.Response({'message': "ботимиздан аввал рўйхатдан ўтгансиз!",
                                      'message_ru': "Вы зарегистрировались раньше нашего бота!"})
        serializer.save()
        return response.Response(
            {'message': "ботимиздан рўйхатдан ўтдингиз!", 'message_ru': "Вы зарегистрировались с нашего бота!"})

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


class DeleteUserAPI(views.APIView):
    def get_queryset(self):
        client = Client.objects.filter(telegram_id=self.kwargs['pk']).first()
        instructor = Instructor.objects.filter(telegram_id=self.kwargs['pk']).first()
        if client:
            return client
        else:
            return instructor

    def delete(self, request, *args, **kwargs):
        obj = self.get_queryset()
        obj.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)
