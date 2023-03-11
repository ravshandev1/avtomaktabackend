from django.urls import path
from .views import InstructorAPI, CarListAPI, RegionListAPI, RatingAPI, IncreaseBalanceAPI, FreeTimeAPI

urlpatterns = [
    path('<int:pk>/', InstructorAPI.as_view()),
    path('regions/', RegionListAPI.as_view()),
    path('cars/', CarListAPI.as_view()),
    path('rating/', RatingAPI.as_view()),
    path('balanse/', IncreaseBalanceAPI.as_view()),
    path('free/', FreeTimeAPI.as_view()),
]
