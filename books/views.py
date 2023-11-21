from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import CustomUserCreationForm  
from allbooks.models import Collection 
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.shortcuts import HttpResponseRedirect
from .models import News


def index(request):
    collections = Collection.objects.all()
    user_signed_up = request.session.pop('user_signed_up', False)
   
    latest_news = News.objects.last()
    return render(request, 'main/index.html', {'collections': collections, 'user_signed_up': user_signed_up, 'latest_news': latest_news})


def welcome(request):
    return render(request, 'main/welcome.html')
def about(request):
    return render(request, 'main/about.html')

def signup(request):
    user_signed_up = False 

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            request.session['user_signed_up'] = True
            messages.success(request, 'You have successfully signed up and logged in!')
            return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})



def book_catalog(request):
    collections = Collection.objects.all()
    return render(request, 'main/book_catalog.html', {'collections': collections})



from django.shortcuts import render

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('welcome') 

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        return render(request, 'main/welcome.html', {'user_logged_out': True})
