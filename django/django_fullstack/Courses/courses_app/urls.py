from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index,name='index'),	
    path('addCourses', views.addCourses,name='addCourses'),	
    path('delCourses/<int:Cid>', views.delCourses,name='delCourses'),
    path('deleteCourse/<int:Cid>', views.deleteCourse,name='deleteCourse'),	   	   
]