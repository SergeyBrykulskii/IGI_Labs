from django.urls import path
from . import views

urlpatterns = [
    path('', views.gym_list, name='gym_list'),
]