from atexit import register
from msilib.schema import CheckBox
from multiprocessing import context
from django.shortcuts import render, redirect
from mysite.forms import RegistionForm
from .models import ToDo
from .forms import ToDoForm, EditForm, completedForm
from django.contrib.auth.models import User


# Create your views here.
def reg(request):
    
    if request.method == 'POST':
        form = RegistionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reg')
    else:
        form = RegistionForm()

    return render(request, 'mysite/index.html', {'form':form})


def completedTodo(request, id):
    #user = request.user
    todoId = ToDo.objects.get(id=id)
    todo_item = ToDo.objects.filter(id=id)
    #item_list = ToDo.objects.filter(user=user)
    form = completedForm(request.POST or None, instance=todoId)
    
    #user = User.objects.get(id=id)
    if form.is_valid():
        
        form.save()
        completed = True
        
       
        return redirect('logged_in')
    
    return render(request, 'mysite/popup.html', {'form':form, 'todoId':todoId, 'todo_item': todo_item})



def logged_in(request):

    user = request.user
    item_list = ToDo.objects.filter(user=user)
    #todo_item = ToDo.objects.all()

    form = ToDoForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.user = request.user
        form.save()
        return redirect('logged_in')
   

    return render(request, 'mysite/logged_in.html', {'form': form, 'item_list': item_list})


   
    # user = request.user
    # item_list = ToDo.objects.filter(user=user)
    # form = ToDoForm(request.POST)
    # if form.is_valid():
    #     user = form.save(commit=False)
    #     user.user = request.user
    #     form.save()
    #     return redirect('logged_in')
   
            
        

def edit(request, id):
    item = ToDo.objects.get(id=id)
    form = EditForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('logged_in')

    return render(request, 'mysite/edit_form.html', {'form':form, 'item':item})


def delete(request, id):
    item = ToDo.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('logged_in')
    return render(request, 'mysite/delete.html', {'item':item})



        