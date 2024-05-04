from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .forms import UserRegister, Login

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('users:profile')

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():            
            form.save()
            # Redirecting for the success page
            messages.success(request, "Deu good, godfather")
            return redirect('users:login')
    
    else:
        form = UserRegister()
    return render(request, 'users/register.html', {'form': form})
    
def login(request):
    if request.user.is_authenticated:
        return redirect('users:profile')
    
    if request.method == 'POST':
        return HttpResponse ('POST TO BE IMPLEMENTED')
    
    form = Login()
    return render (request,'users/login.html',{'form':form})


@login_required
def profile(request):
    if request.method == 'POST':
        return HttpResponse ('POST TO BE IMPLEMENTED')
    
    return render (request,'users/register.html')
