from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="digital_library_home"),
]