from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class SignUpView(CreateView):
    form = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = 'login'