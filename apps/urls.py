from django.urls import path, include


urlpatterns = [
    path('client/', include('client.urls')),
    path('instructor/', include('instructor.urls')),
    path('session/', include('session.urls')),
]
