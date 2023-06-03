from django.shortcuts import render
from django.http import JsonResponse
import random

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    password_generated = ''

    length = int(request.POST.get('length'))

    if request.POST.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.POST.get('special'):
        characters.extend(list('@-_$%&/()=¿?¡!'))

    if request.POST.get('numbers'):
        characters.extend(list('0123456789'))

    for i in range(length):
        password_generated += random.choice(characters)

    return JsonResponse({'password': password_generated})
