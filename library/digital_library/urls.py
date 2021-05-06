from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="digital_library_home"),
    path('about', views.about, name="digital_library_about"),
    path('books', views.show_books, name="digital_library_book_list"),
    path('books/<int:id>', views.show, name="digital_library_book")
]