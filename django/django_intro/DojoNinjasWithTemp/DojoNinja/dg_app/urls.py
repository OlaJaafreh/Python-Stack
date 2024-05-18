from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ninja/', views.ninja, name='ninja'),
    path('dojo/', views.dojo, name='dojo'),
]
