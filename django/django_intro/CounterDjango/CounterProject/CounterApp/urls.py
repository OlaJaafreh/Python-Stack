from django.urls import path     
from . import views
urlpatterns = [
    path('', views.Counter),	 
    path('destroy_session', views.distroy),	
    path('Reset', views.Reset),	 
    path('IncByUser', views.addUser),	 
    path('IncBy2', views.add2),
]