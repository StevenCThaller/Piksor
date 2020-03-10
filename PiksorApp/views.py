from django.shortcuts import render, redirect
from .models import PixarCharacter, Series
# Create your views here.


def index(request):
    context = {
        "characters": PixarCharacter.objects.all()
    }
    return render(request, "index.html", context)


def one_series(request, series_id):
    context = {
        "this_series": Series.objects.get(id=series_id)
    }
    return render(request, "series.html", context)
