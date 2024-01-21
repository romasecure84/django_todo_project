from django.shortcuts import render
from todo.models import Todo
from django.http import Http404

def home_view(request):
    todos = Todo.objects.filter(
        is_active=True
        )
    context = dict(
        todos=todos
    )
    return render(request, 'todo/todo_list.html', context)

def todo_detail_view(request, id):
    try:
        todo = Todo.objects.get(pk=id)
        context = dict(
          todo=todo
          )
        return render(request, 'todo/todo_detail.html', context)
    except Todo.DoesNotExist:
        raise Http404