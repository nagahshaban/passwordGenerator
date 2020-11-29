from django.http import HttpResponse
from django.shortcuts import render, redirect
from string import digits, ascii_lowercase, ascii_uppercase, ascii_letters
from random import choice
from . import validations


def home(request):
    return render(request, 'generators/home.html')


def passwords(request):
    data = request.GET
    if data:
        length = data.get('length')
        upper = data.get('upper')
        number = data.get('number')
        special = data.get('special')
        chars = ascii_letters
        if number:
            chars += digits
        if special:
            chars += '$#%^&*()@!'
        password = validations.get_password(chars, length, upper)
        is_valid = validations.validate_password(password)
        while not is_valid:
            password = validations.get_password(chars, length, upper)
            is_valid = validations.validate_password(password)
            if is_valid:
                break
        return render(request, 'generators/passwords.html', context={'password': password})
    else:
        return redirect('home')


def generate_password(request):
    data = request.GET
    if data:
        length = data.get('length', 10)
        upper = data.get('upper')
        number = data.get('number')
        special = data.get('special')
        chars = ascii_lowercase
        if upper:
            chars += ascii_uppercase
        if number:
            chars += digits
        if special:
            chars += '$#%^&*()@!'

        password = ''
        for i in range(int(length)):
            password += choice(chars)
        return render(request, 'generators/passwords.html', context={'password': password})
    else:
        return redirect('home')


def about(request):
    return HttpResponse("About Page !")