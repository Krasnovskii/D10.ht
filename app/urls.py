from django.urls import path

from . import views

urlpatterns = [
    path('car/', views.Car.as_view(), name='car')
    ]
