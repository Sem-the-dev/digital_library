from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserSignupForm

# Create your views here.

def signup(req):
    if req.method =='POST':
        form = UserSignupForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned.data.get('username')
            messages.success(req, f'Welcome, {username}')
            return redirect('digital-library-home')
    else:
        form = UserSignupForm()
    data = {'form': form}
    return render(req, 'signup.html', data)