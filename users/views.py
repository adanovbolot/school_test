from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from django.views.generic import CreateView
from users.forms import CustomUserCreationForm


class SigUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('school_list')
    template_name = 'account/register.html'


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})
