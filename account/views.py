from django.shortcuts import render

# Create your views here.
def user_login(request):
    return render(request, 'account/login.html')

def register(request):
    return render(request, 'account/register.html')

def forget(request):
    return render(request, 'account/forget.html')