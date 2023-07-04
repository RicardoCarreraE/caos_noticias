from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm
from .models import Task, NuevoUsuario
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request,'index.html')
    
'''def registro(request):
    if request.method == 'GET':
        return render(request, 'registro.html',{
            'form': UserCreationForm
        })
    else:
        if request.POST['password1']== request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'registro.html',{
                    'form':UserCreationForm,
                    "error": 'User already exists'
                })
        return render(request, 'registro.html',{
            'form':UserCreationForm,
            "error": 'Password do not match'
        })'''

@login_required
def tasks(request):
    tasks = Task.objects.filter(user = request.user, datecompleted__isnull=True)
    return render(request, 'tasks.html', {'tasks': tasks})

@login_required
def tasks_completed(request):
    tasks = Task.objects.filter(user = request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'tasks.html', {'tasks': tasks})
                
@login_required
def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': TaskForm
        })
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
             return render(request, 'create_task.html', {
                'form': TaskForm,
                'error': 'Por favor provee datos correctos'
            })

@login_required
def task_detail(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = TaskForm(instance=task)
        return render(request, 'task_detail.html',{'task': task, 'form': form})
    else:
        try:
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'task_detail.html', {
                'task':task, 'form': form, 'error': "Error updating task "
            })

@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method =='POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')
    
@login_required   
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method =='POST':
        task.delete()
        return redirect('tasks')
    
@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('index')


def iniSesion(request):
    if request.method == 'GET':
         return render(request, 'iniSesion.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
              return render(request, 'iniSesion.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o password es incorrecto'
            })
        else:   
            login(request, user)
            return redirect('tasks')
            

def DEPORTE(request):
    return render(request, 'DEPORTE.html')

def POPULAR(request):
    return render(request, 'POPULAR.html')

def POLITICA(request):
    return render(request, 'POLITICA.html')

def Formulario(request):
    return render(request, 'Formulario.html')


#Funcion de registro
def registro(request):
    if request.method == 'GET':
        #si el metodo es GET, vuelve a registro.html y muestra el formulario
        return render(request, 'registro.html', {
            'form': UserCreationForm
        })
    else:
        #Si el metodo es POST, valida ambas contraseñas que sean iguales para pasar a
        #guardar el objeto completo
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                password=request.POST['password1'])     
                 
                nombre           = request.POST["nombre"]
                aPaterno         = request.POST["paterno"]
                aMaterno         = request.POST["materno"]
                usuario          = request.POST['username']    
                email            = request.POST["email"]
                fechaNac         = request.POST["fechaNac"]
                telefono         = request.POST["telefono"]
                direccion        = request.POST["direccion"]
                password1       = request.POST["password1"]
                password2       = request.POST["password2"]
                activo           = '1'
                #en cada variable, luego en la variable objeto guarda todo juntito
                    
                objeto = NuevoUsuario.objects.create(
                                            nombre=nombre,
                                            apellido_paterno=aPaterno,
                                            apellido_materno=aMaterno,
                                            usuario=usuario,
                                            email=email,
                                            fecha_nacimiento=fechaNac,
                                            telefono=telefono,
                                            direccion=direccion,
                                            password1=password1,   
                                            password2=password2,                                  
                                            activo=1)
                #lo tira a la base de datos con .save()
                objeto.save()
                login(request, objeto)
                return render (request, 'iniSesion.html',{
                    'form': UserCreationForm,
                    "error": 'usuario creado'
                })
            except IntegrityError:
                return render (request, 'registro.html',{
                    'form': UserCreationForm,
                    "error": 'El usuario ya existe'
                })
    return render (request, 'registro.html',{
                    'form': UserCreationForm,
                    "error": 'Las contraseñas no coinciden'
                })