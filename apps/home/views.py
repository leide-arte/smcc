from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView( LoginRequiredMixin, TemplateView):
    template_name="home/index.html"

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        return context

        
def sair(request):
    logout(request)
    return redirect('login')