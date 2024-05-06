from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def login_view(request): 
    if request.method == "POST": 
        username = request.POST["username"] 
        password = request.POST["password"] 
        user = authenticate(request, username=username, password=password) 
        if user: 
            login(request, user) 
            return redirect(reverse("index")) 
        else: 
            return render(request, "usuario/login.html", { "msj": "Credenciales incorrectas" }) 
    return render(request, "usuario/login.html")

def logout_view(request): 
    logout(request) 
    return redirect(reverse("index")) 

#para registrar nuevo usuario
def crear_usuario(request):
    if request.method == 'GET':
        return render(request, 'usuario/registro_user.html',{
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            #si las contraseñas son coincidentes registramos el usuario
            try:
                usuario = User.objects.create_user(username=request.POST['username'],
                                                   password=request.POST['password1'])
                usuario.save()
                login(request, usuario)
                return redirect('index')
            
            except IntegrityError:
                return render(request, 'usuario/registro_usuario.html',{
                    'form': UserCreationForm,
                    'error': "El usuario ingresado ya existe."
                })
        else:
            return render(request, 'usuario/registro_usuario.html', {
                'form': UserCreationForm,
                'error': "Las contraseñas no coiciden."
            })
