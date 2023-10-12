from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from django.contrib import messages
from .forms import TodoForm
from .models import Todo

# Create your views here.
def home(request):
        todos = Todo.objects.all()
        return render(request, 'home.html', {'todos': todos})

@require_http_methods(['POST'])
def addTodo(request):
        todo = None
        title = request.POST.get('title', '')

        if title:
                todo=Todo.objects.create(title=title)
        
        return render(request, 'aap/partials/todo.html', {'todo': todo})