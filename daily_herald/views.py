from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class HomePageView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'daily_herald/homepage.html'
