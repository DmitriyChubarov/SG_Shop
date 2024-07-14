from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView

from . models import Tshirt

class Tshirtlist(ListView):
    model = Tshirt
    template_name = 'tshirlist.html'

class Home(TemplateView):
    template_name = 'home.html'
