from django.urls import path
from .views import validate_pesel

urlpatterns = [
    path('', validate_pesel, name='validate_pesel'),
]
