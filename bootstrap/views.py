from django.shortcuts import render

# Create your views here.
def home(request):
    user_info = request.user
    return render(request, 'index.html', {
        "user_info": user_info,
    })