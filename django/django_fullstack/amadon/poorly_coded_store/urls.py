from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('checkout/', views.checkout,name='checkout'),
    path('chre/', views.chre,name='chre'),
    path('chre/delete/', views.delete,name='delete')

]
