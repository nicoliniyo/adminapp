from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.



def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Usuario ya existe!'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Password no son iguales!'
        })


def base(request):
    return render(request, 'base.html')


def signout(request):
    logout(request)
    return redirect('index')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html',
                      {
                          'form': AuthenticationForm
                      })
    else:
        print(request.POST)
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html',
                          {
                              'form': AuthenticationForm,
                              'error': 'Usuario o contraseña incorrectos'
                          })
        else:
            login(request, user)
            return redirect('index')


