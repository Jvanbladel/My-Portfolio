from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .weather_api import get_weather, get_location_name

# Create your views here.


def weather(request):
    location = request.GET.get("location", "")

    if location:
        weather_data = get_weather(location)
        location_name = get_location_name(location)
        if weather_data:
            context = {"weather_data": weather_data, "location_name": location_name}
            return render(request, "weather.html", context)
        else:
            context = {"weather_data": None, "location_name": location_name}
            return render(request, "weather.html", context)
    else:
        return render(
            request, "weather.html"
        )  # If location is not provided, render the empty template


def risk_analyzer(request):
    return render(request, "risk_analyzer.html")


def auction_house(request):
    return render(request, "auction_house.html")


def immunization_compliance(request):
    return render(request, "immunization_compliance.html")


def starving_steve(request):
    return render(request, "starving_steve.html")


def epic_tanks(request):
    return render(request, "epic_tanks.html")


def battle_vessel(request):
    return render(request, "battle_vessel.html")
