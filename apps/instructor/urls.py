from django.urls import path
from .views import InstructorAPI, CarListAPI, RegionListAPI, RatingAPI, IncreaseBalanceAPI

urlpatterns = [
    path('<int:pk>/', InstructorAPI.as_view()),
    path('regions/', RegionListAPI.as_view()),
    path('cars/', CarListAPI.as_view()),
    path('rating/', RatingAPI.as_view()),
    path('balanse/', IncreaseBalanceAPI.as_view()),
]
