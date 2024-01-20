from django.shortcuts import render
from todo.models import Todo
# from django.http import HttpResponse

def home_view(request):
    todos = Todo.objects.filter(is_active=True)
    context = dict(
        todos=todos
    )
    return render(request, 'todo/todo_list.html', context)
