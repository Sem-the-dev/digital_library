from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="digital-library-home"),
    path('about', views.about, name="digital-library-about"),
    path('books', views.show_books, name="digital-library-book-list"),
    path('books/<int:id>', views.show_one, name="digital-library-book")
    
]