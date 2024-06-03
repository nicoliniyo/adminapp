from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

# Create your views here.

def get_username(email):
    """Extracts the username from an email address.

    Args:
        email: A string containing the email address.

    Returns:
        The username portion of the email address, or None if the email is invalid.
    """
    if "@" not in email:
        return None  # Email doesn't contain "@" symbol

    username_part = email.split("@")[0]
    return username_part

def signup(request):
    if request.method == 'GET':
        print('Handling GET request - Displaying signup form')
        return render(request, 'signup.html', {'form': UserCreationForm})
    else:
        print('Handling POST request - Processing signup data')
        if request.POST['password1'] == request.POST['password2']:
            username = get_username(request.POST['username'])
            print(f'Extracted username: {username}')
            try:
                user = User.objects.create_user(
                    email=request.POST['username'],
                    username=username,
                    password=request.POST['password1'])
                user.save()
                login(request, user)
                print('User created successfully, redirecting to Tasks')
                return redirect('tasks')
            except Exception as e:
                print(f"An error occurred: {e}")
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Usuario ya existe!'
                })
        else:
        
            print('Passwords do not match')
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


