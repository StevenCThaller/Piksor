from django.shortcuts import render, redirect
from .models import PixarCharacter, Series
# Create your views here.


def index(request):
    context = {
        "characters": PixarCharacter.objects.all(),
        "all_series": Series.objects.all()
    }
    return render(request, "index.html", context)


def one_series(request, series_id):
    context = {
        "this_series": Series.objects.get(id=series_id)
    }
    return render(request, "series.html", context)


def addcharacter(request):
    # Get the character name from the form
    char_name = request.POST['name']
    # Get the character height form the form
    char_height = request.POST['height']
    # Get the character description from the form
    char_description = request.POST['description']
    # Get the series with the id that's in the form
    char_series = Series.objects.get(id=request.POST['series'])

    # Now let's take these things and actually CREATE this object.
    PixarCharacter.objects.create(
        name=char_name, height=char_height, description=char_description, series=char_series)

    # Awesome! we created the character. now let's redirect back to the main page!
    return redirect('/')


def addseries(request):
    # Get the series name from the form
    series_name = request.POST['series_name']
    # Get the series release date from the form
    series_date = request.POST['first_release_date']
    # Get the series description from the form
    series_description = request.POST['description']

    # Now let's take these things and actually CREATE this object!
    Series.objects.create(series_name=series_name,
                          first_release_date=series_date, description=series_description)

    # Sweet! Now let's go back to the main page!
    return redirect('/')
