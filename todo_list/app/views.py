from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http.response import HttpResponse
from .models import Todo

# Create your views here.
def todos(request):
        todos = Todo.objects.all()
        return render(request, 'todo/todos.html', {'todos': todos})

@require_http_methods(['POST'])
def addTodo(request):
        todo = None
        title = request.POST.get('title', '')

        if title:
                todo=Todo.objects.create(title=title)
        
        return render(request, 'aap/partials/todo.html', {'todo': todo})

@require_http_methods(['GET', 'POST'])
def editTodo(request, pk):
        todo = Todo.objects.get(pk=pk)
        if request.method == "POST":
                todo.title = request.POST.get('title', '')
                todo.save()
                return render(request, 'todo/partials/todo.html', {'todo': todo})
        return render(request, 'todo/partials/edit.html', {'todo': todo})

