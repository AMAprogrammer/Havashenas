from django.urls import path 
from .views import get_weather

urlpatterns = [
    path('<str:city>/<str:time>',get_weather,name='weather')
]
