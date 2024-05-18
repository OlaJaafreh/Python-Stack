from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	   
    path('GoldTotal', views.GoldTotal),	 
    path('delete', views.deleteed),
    path('yourgold', views.process_money),	
]