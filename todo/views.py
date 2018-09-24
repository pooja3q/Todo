from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm, NewTodoForm


def index(request):
    todo_list = Todo.objects.order_by('id')

   # form = TodoForm()
    form = NewTodoForm()
    context = {'todo_list': todo_list, 'form': form}
    return render(request, "todo/index.html", context)


def addTodo(request):
   # form = TodoForm(request.POST)

    newtodoform = NewTodoForm(request.POST)
    if newtodoform.is_valid():
        newtodoform.save()

    return redirect('index')

#new_todo = Todo(text=form.cleaned_data['text'])
# #new_todo.save()


def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    return redirect('index')

def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('index')

def deleteAll(request):
    Todo.objects.all().delete()
    return redirect('index')
