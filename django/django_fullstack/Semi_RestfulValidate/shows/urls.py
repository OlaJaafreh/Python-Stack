from django.urls import path     
from . import views
urlpatterns = [
    path('shows/new', views.addshow), 
    path('shows', views.allshow,name='allshow'), 
    path('shows/<int:id>', views.tvshow,name='tvshow'), 
    path('shows/<int:id>/edit', views.editshow,name='editshow'), 
    path('shows/<int:id>/delete', views.delete,name='delete'), 
]