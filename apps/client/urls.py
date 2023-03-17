from django.urls import path
from .views import ClientAPI, DeleteUserAPI, TextUAPI, TextRAPI

urlpatterns = [
    path('<int:pk>/', ClientAPI.as_view()),
    path('delete/<int:pk>/', DeleteUserAPI.as_view()),
    path('text-r/<int:pk>/', TextRAPI.as_view()),
    path('text-u/<int:pk>/', TextUAPI.as_view()),
]
