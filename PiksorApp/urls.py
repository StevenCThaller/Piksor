from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('series/<int:series_id>', views.one_series),
    path('addcharacter', views.addcharacter),
    path('addseries', views.addseries)
]
