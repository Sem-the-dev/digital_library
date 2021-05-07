from .models import Book
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .forms import BorrowBookForm, NewBookForm


def home(req):
    return render(req, 'home.html')

def about(req):
    return render(req, 'about.html')

@login_required
def show_books(req):
    books = {'book': Book.objects.all()}
    return render(req, 'books.html', books)

@login_required
def create(req):
    if req.method == 'POST':
        book = NewBookForm(req.POST)
        if book.is_valid():
            id = book.save().id
            return redirect("digital-library-book", id=id)
    else:
        form = NewBookForm()
    data = {'form': form}
    return render(req, 'new.html', data)

@login_required
def show_one(req, id):
    #book = Book.objects.get(pk=id)
    book = get_object_or_404(Book, pk=id)
    if req.method == 'POST':
        form = BorrowBookForm(req.POST)
        if form.is_valid():
            if book.borrower == None: 
                book.borrower = req.user
            else:
                book.borrower = None
            book.save()
            return redirect("digital-library-book", id = id)

    else:
        form = BorrowBookForm(initial={'borrower': req.user})
        data = {
            "book": book,
            "form": form
        }
    return render(req, 'show.html', data)
    #return HttpResponse(f'<p>Read {books.title}</p>')



def not_found_404(req, exception):
    #data = { 'err': exception }
    return render(req, '400.html')

def server_error_500(req):
    return render(req, '500.html')
