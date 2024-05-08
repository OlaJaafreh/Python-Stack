from django.urls import path
from .  import views
urlpatterns = [path('',views.root), 
               path('blog',views.index),
               path('blog/New',views.New),
               path('blog/Create',views.Create),
               path('blog/<int:Number>',views.show),
               path('blog/<int:Number>/edit',views.edit),
               path('blog/<int:Number>/delete',views.destroy),
               path('Jsonn',views.JasonMethod),]
