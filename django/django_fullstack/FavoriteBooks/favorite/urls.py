from django.urls import path     
from . import views

urlpatterns = [
    path('', views.loginPage,name='loginPage'),	
    path('log', views.login,name='login'),	   
    path('register', views.register,name='register'),
    path('books', views.AddBook,name='AddBook'),	
    path('books/add/<int:U_id>', views.AddMyBook,name='AddMyBook'),
    path('books/<int:U_id>/<int:B_id>', views.EditBook,name='EditBook'),
    path('book/<int:O_id>', views.OtherBook,name='OtherBook'),
    path('books/<int:U_id>/<int:B_id>/edit', views.EditMyBook,name='EditMyBook'),
    # path('books/<int:U_id>/<int:B_id>', views.deleteBook,name='deleteBook'),
    path('books/<int:U_id>/<int:B_id>/delete', views.deleteMyBook,name='deleteMyBook'),
    

    
]