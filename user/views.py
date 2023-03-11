from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from user.forms import CustomUserCreationForm


# Create your views here.
class SignUpView(CreateView):
    template_name = 'sign_up.html'
    form_class = CustomUserCreationForm
    model = get_user_model()
    success_url = reverse_lazy('login')

