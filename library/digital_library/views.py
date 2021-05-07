from .models import Book
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.

# books_data = [
#     {'id': 1, 'title': 'Harry Potter'},
#     {'id': 2, 'title': 'The Meaning of Life'}
# ]

# books_data = [
#     { 'id': 1, 'title': 'Life, the Universe and Everything', 'author': 'Douglas Adams'},
#     { 'id': 2, 'title': 'The Meaning of Liff' 'author': 'Douglas Adams'},
#     { 'id': 3, 'title': 'The No. 1 Ladies\' Detective Agency' 'author': 'Alexander McCall Smith'}
# ]

def home(req):
    return render(req, 'home.html')

def about(req):
    return render(req, 'about.html')

def show_books(req):
    books = {'book': Book.objects.all()}
    return render(req, 'books.html', books)

def show_one(req, id):
    # books = get_object_or_404(Book, pk=id)
    books = Book.objects.get(pk=id)
    # return render(req, 'show.html', books)
    return HttpResponse(f'<p>Read {books.title}</p>')

def not_found_404(req, exception):
    #data = { 'err': exception }
    return render(req, '400.html')

def server_error_500(req):
    return render(req, '500.html')
