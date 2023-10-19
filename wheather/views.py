from django.shortcuts import render
from requests import get
from .local_api import api_key
# Create your views here.


def get_weather(request,city,time):


    resault = get(f"http://api.weatherapi.com/v1/{time}.json?key={api_key}&q={city}")
    
    data = resault.json()
    
    return render(request,'weather.html',{'data':data})