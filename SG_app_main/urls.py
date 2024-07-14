from django.urls import path, include
from SG_app_main import views
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.Home.as_view(),name='home'),
    path('tshirt/', views.Tshirtlist.as_view(),name='tshirlist'),

]

