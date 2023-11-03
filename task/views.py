from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
# Create your views here.
from django.contrib.messages import constants
from django.contrib import messages
from datetime import datetime

def task(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html', context={'tasks': tasks})

def add_task(request):
    if request.method == "GET":
        return render(request, 'add_task.html')
    
    elif request.method == "POST":
        nome_task = request.POST.get('nome_task')
        descricao = request.POST.get('descricao')
        data_inicio = request.POST.get('data_inicio')
        data_final = request.POST.get('data_final')
        
        if nome_task == "":
            messages.add_message(request, constants.WARNING, 'Ops! Parece que você esqueceu de informar o nome da Task.')
            return redirect('/tasks/add_task/')
           
        elif len(nome_task) > 25:
            messages.add_message(request, constants.WARNING, 'Ops! Você excedeu o limite máximo de 25 caracteres.')
            return redirect('/tasks/add_task/')
        
        elif len(descricao) > 244:
            messages.add_message(request, constants.WARNING, 'Ops! Você excedeu o limite máximo de 244 caracteres.')
            return redirect('/tasks/add_task/')
        
        elif not data_final:
            messages.add_message(request, constants.WARNING, 'Ops! Parece que você ainda não informou a data final.')
            return redirect('/tasks/add_task/')
          
        else:
            try:
                tasks = Task.objects.create(
                    nome=nome_task,
                    descricao=descricao,
                    data_inicio=data_inicio,
                    data_final=data_final
                )
                    
                tasks.save()
                    
                messages.add_message(request, constants.SUCCESS, 'Task criada com sucesso')
                return redirect('/tasks/add_task/')
                
            except:
                messages.add_message(request, constants.ERROR, 'Erro inesperado')
                return redirect('/tasks/add_task/')
                
def delete_task(request, id):
    tasks = Task.objects.get(pk=id)
    if request.method == "GET":
        return render(request, 'delete_task.html', context={'tasks': tasks})
    
    elif request.method == "POST":
        tasks.delete()
        return redirect('/tasks/')
    
def update_task(request, id):
    if request.method == "GET":
        tasks = Task.objects.get(pk=id)
        return render(request, 'update_task.html', context={'tasks': tasks})
    
    elif request.method == "POST":
        tasks = Task.objects.filter(pk=id)
        
        update_nome = request.POST.get('update_nome')
        update_descricao = request.POST.get('update_descricao')
        update_data_final = request.POST.get('update_data_final')
        
        if update_nome == "":
            messages.add_message(request, constants.WARNING, 'Ops! Parece que você esqueceu de informar o nome da Task.')
            return redirect(f'/tasks/update_task/{id}')
               
        elif len(update_nome) > 25:
            messages.add_message(request, constants.WARNING, 'Ops! Você excedeu o limite máximo de 25 caracteres.')
            return redirect(f'/tasks/update_task/{id}')
        
        elif len(update_descricao) > 244:
            messages.add_message(request, constants.WARNING, 'Ops! Você excedeu o limite máximo de 25 caracteres.')
            return redirect(f'/tasks/update_task/{id}')
        
        else:
            try:
                tasks.update(
                    nome=update_nome,
                    descricao=update_descricao,
                    data_final=update_data_final
                )
                return redirect('/tasks/') 
            except:
                return redirect('/tasks/') 
            
def read_task(request, id):
    tasks = Task.objects.get(pk=id)
    return render(request, 'read_task.html', context={'tasks':tasks})