from django.urls import path     
from . import views
urlpatterns = [
    path('', views.loginPage,name='loginPage'),	
    path('log', views.login,name='login'),	 	   
    path('register', views.register,name='register'), 
    path('addBooks', views.AddBooks,name='addBooks'), 
    path('books', views.books,name='books'), 
    path('otherBook/<int:BookId>', views.otherBook,name='otherBook'), 
    path('userBook/<int:BookId>', views.userBook,name='userBook'),
    path('confirmBook/<int:BookId>', views.confirmBook,name='confirmBook'),
    path('EdituserBook/<int:BookId>', views.EdituserBook,name='EdituserBook'),
    path('DeleteuserBook/<int:BookId>', views.DeleteuserBook,name='DeleteuserBook'),
    path('AddToFavorite/<int:BookId>', views.AddToFavorite,name='AddToFavorite'),
    path('RemoveFromFavorite/<int:BookId>', views.RemoveFromFavorite,name='RemoveFromFavorite'),
]