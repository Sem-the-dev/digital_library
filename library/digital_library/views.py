from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

books_data = [
    {'id': 1, 'title': 'Harry Potter'},
    {'id': 2, 'title': 'The Meaning of Life'}
]

# books_data = [
#     { 'id': 1, 'title': 'Life, the Universe and Everything', 'author': 'Douglas Adams'},
#     { 'id': 2, 'title': 'The Meaning of Liff' 'author': 'Douglas Adams'},
#     { 'id': 3, 'title': 'The No. 1 Ladies\' Detective Agency' 'author': 'Alexander McCall Smith'}
# ]

def home(req):
    data = {'books': 'books_data'}
    return render(req, 'home.html', data)

# def show(req, id):
#     return render(req, )