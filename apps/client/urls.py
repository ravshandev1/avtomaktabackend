from django.urls import path
from .views import ClientAPI, DeleteUserAPI

urlpatterns = [
    path('<int:pk>/', ClientAPI.as_view()),
    path('delete/<int:pk>/', DeleteUserAPI.as_view()),
]
