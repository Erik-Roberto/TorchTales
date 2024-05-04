from django.urls import path

from .views import register, login, profile

app_name = 'users'

urlpatterns = [
    path('profile/',profile, name= 'profile'  ),
    path('register/', register, name='register'),
    path('login/',login, name = 'login')
]