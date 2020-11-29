
from django.urls import path
from .views import *   # home, about, passwords, ...

# entry points
urlpatterns = [

    path('', home, name='home'),
    path('passwords/', passwords, name='passwords'),
    path('generate_password/', generate_password, name='generate_password'),
    path('about/', about, name='about'),
]