from .models import Car
from django.views.generic import ListView


class Car(ListView):
    model = Car
    templates_name = 'index.html'