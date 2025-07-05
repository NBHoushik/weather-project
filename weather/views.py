import requests
from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from django.contrib import messages
# Create your views here.


def index(request):
  weather_data=None
  if request.method=="POST":
    city=request.POST.get("city")
    current_day=datetime.now().strftime("%A")
    current_date=datetime.now().strftime("%d %B %Y")
    API_KEY="3328620db862aa503394763f958506d0"
    search_url="http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID={}".format(city,API_KEY)
    data=requests.get(search_url).json()
    if data["cod"]==200: # (or) if data.status_code==200: data=data.json()
      weather_data={
        "city":city,
        "weather":data["weather"][0]["description"],
        "temp":data["main"]["temp"],
        "humidity":data["main"]["humidity"],
        "wind_speed":data["wind"]["speed"]
      }
      return render(request,"weather/index.html",{"weather_data":weather_data,"current_day":current_day,"current_date":current_date})
    else:
      d="Enter valid city"
      return render(request,"weather/index.html",{"message":d})
  else:
    return render(request,"weather/index.html",{"weather_data":weather_data})
    
 