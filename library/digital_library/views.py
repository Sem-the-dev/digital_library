from .models import Book
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required


def home(req):
    return render(req, 'home.html')

def about(req):
    return render(req, 'about.html')

@login_required
def show_books(req):
    books = {'book': Book.objects.all()}
    return render(req, 'books.html', books)
@login_required
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
