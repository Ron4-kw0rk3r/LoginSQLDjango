
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from .models import Usracceso
from .models import Acceso

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.hashers import check_password
from .models import Dacceso 


def main(request):
    return render(request, 'portflycrab/main.html')



def loginv(request):
    return render(request, 'portflycrab/loginv.html')
from django.http import HttpResponse

def validator(request):
    with open('portflycrab/static/validator.js', 'r') as file:
        js_code = file.read()
    return HttpResponse(js_code, content_type='application/javascript')


def logout_view(request):
    # Eliminar la sesión del usuario
    request.session.flush()
    return redirect('main')

def register(request):
    return render(request, 'portflycrab/register.html')


def portindex(request):

    return render(request, 'portflycrab/portindex.html')


def index(request):
    return render(request, 'portflycrab/index.html' )


def about(request):
    return render(request, 'portflycrab/about.html')




def transformpdf(request):
    return render(request, 'portflycrab/algpdf.html')



def login_view(request):
    if request.method == 'POST':
        correo = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = Dacceso.objects.get(correo=correo)
            if check_password(password, user.password):
                # Establecer manualmente la sesión del usuario
                request.session['user_id'] = user.id
                request.session['user_email'] = user.correo
                return redirect('portindex')  # Asegúrate de que 'portindex' esté definido en tus patrones de URL
            else:
                return render(request, 'loginv.html', {'error_message': 'Correo o contraseña incorrectos'})
        except Acceso.DoesNotExist:
            return render(request, 'loginv.html', {'error_message': 'Correo o contraseña incorrectos'})

    return render(request, 'loginv.html')


def register_user(request):
    if request.method == 'POST':
        # Obtener los datos del formulario enviado por el cliente
        data = request.POST
        nombre = data.get('username')
        correo = data.get('email')
        password = data.get('password')
        seed = data.get('seed')

        # Crear un nuevo usuario en la base de datos
        try:
            usuario = Usracceso(nombre=nombre, correo=correo,password=password , seed=seed)
            usuario.save()
            return JsonResponse({'success': True, 'message': 'Usuario registrado exitosamente'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return render(request, 'register.html')
