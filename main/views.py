from django.shortcuts import render
from main.models import *
from django.http import HttpResponseRedirect

# Create your views here.

def main(request):
    todo = Todo.objects.all()
    return render(request, 'index.html', {'todo': todo})


def create(request):
    if request.method == "POST":
        todo = Todo.objects.all()
        new_todo = Todo()
        new_todo.title = request.POST.get('title')
        new_todo.description = request.POST.get('description')
        tt = []
        for i in todo:
            tt.append(i.title)
        if new_todo.title in tt:
            return HttpResponseRedirect('/')
        else:
            new_todo.save()
            return HttpResponseRedirect('/')

def delete_letter(request, id):
    todo = Todo.objects.get(id=id)
    deleted_todo = Delete()
    deleted_todo.deleted_title = todo.title
    deleted_todo.deleted_description = todo.description
    deleted_todo.save()
    todo.delete()
    return HttpResponseRedirect('/')

def edit_letter(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.save()
        return HttpResponseRedirect('/')
    return render(request, 'edit.html', {'todo': todo})

def cart(request):
    deleted_todo = Delete.objects.all()
    return render(request, 'cart.html', {'deleted_todo': deleted_todo})

def reestablish(request, id):
    delete_todo = Delete.objects.get(id=id)
    todo=Todo()
    todo.title = delete_todo.deleted_title
    todo.description = delete_todo.deleted_description
    todo.save()
    delete_todo.delete()
    return HttpResponseRedirect('/')

def delete1(request, id):
    todo = Delete.objects.get(id=id)
    todo.delete()
    return HttpResponseRedirect('/cart')

def elected(request):
    elected_todo = Elected.objects.all()
    return render(request, 'elected.html', {'elected_todo': elected_todo})

def elected_letter(request, id):
    todo = Todo.objects.get(id=id)
    elected_item = Elected.objects.all()
    elected_todo = Elected()
    elected_todo.elected_title = todo.title
    elected_todo.elected_description = todo.description
    tt = []
    for i in elected_item:
        tt.append(i.elected_title)
    if elected_todo.elected_title in tt:
        return HttpResponseRedirect('/')
    else:
        elected_todo.save()
        return HttpResponseRedirect('/')

def elected_reestablish(request, id):
    todo = Elected.objects.get(id=id)
    todo.delete()
    return HttpResponseRedirect('/elected')