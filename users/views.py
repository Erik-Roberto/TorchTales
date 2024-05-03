from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return HttpResponse('ALREADY LOGGED')
    if request == 'POST':
        return HttpResponse('POST NOT IMPLEMENTED')
    else:
        form = UserRegister()
    return render(request, 'users/register.html', {'form': form})
    