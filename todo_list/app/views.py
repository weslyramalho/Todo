from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TodoForm
from .models import Todo

# Create your views here.
def home(request):
        return render(request, 'home.html')
