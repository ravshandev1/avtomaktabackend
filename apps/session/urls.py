from django.urls import path
from .views import FilterCreateAPI, CategoryAPI, UserFilterAPI, SessionListAPI, IsFinishedSessions, SessionDetail, \
    PriceAPI, PriceListAPI, PercentAPI, SessionLocationAPI, TextAPI

urlpatterns = [
    path('', FilterCreateAPI.as_view()),
    path('categories/', CategoryAPI.as_view()),
    path('user/', UserFilterAPI.as_view()),
    path('price/', PriceAPI.as_view()),
    path('percent/', PercentAPI.as_view()),
    path('price/list/', PriceListAPI.as_view()),
    path('<int:pk>/', SessionListAPI.as_view()),
    path('finished/<int:pk>/', IsFinishedSessions.as_view()),
    path('detail/<int:pk>/', SessionDetail.as_view()),
    path('location/<int:pk>/', SessionLocationAPI.as_view()),
    path('text/<int:pk>/', TextAPI.as_view()),
]
