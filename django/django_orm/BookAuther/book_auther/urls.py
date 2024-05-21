from django.urls import path     
from . import views
urlpatterns = [
    path('', views.bookhtml,name='bookhtml'),	
    path('authors', views.authorhtml,name='authorhtml'),  
    path('newbook', views.book),	
    path('newauthor', views.author), 
    path('books/<int:id>', views.bookdet,name='bookdet'), 
    path('author/<int:id>', views.authordet,name='authordet'), 
    path('books/addbookauthor/<int:id>', views.bookdetAdd), 
    path('author/addauthorbook/<int:id>', views.authordetAdd),
]