from .views import GetUserSchedule
from django.urls import path

urlpatterns = [
    path('api/schedule', GetUserSchedule.as_view(), name='schedule'),
]
