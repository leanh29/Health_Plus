from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.views.generic import TemplateView, DetailView
from project import utilities
from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings
import requests
from bs4 import BeautifulSoup
import datetime

# @login_required
# def home(request):
#     context = {'permissions': utilities.get_user_permissions(request.user)}
#     return render(request, 'home.html', context)


# def index(request):
    # return render(request, 'index.html')


def crawNewsData(url):
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.content, "html.parser")
    crawed = soup.findAll('span', class_='font24')
    data = {}
    i = 1
    for item in crawed:
        data.update({'date':datetime.date.today})
        if i==1:
            data.update({'case_vn': item.text})
        if i==3:
            data.update({'recoverd_vn': item.text})
        if i==4:
            data.update({'death_vn':item.text})
        if i==5:
            data.update({'case_w':item.text})
        if i==7:
            data.update({'recoverd_w':item.text})
        if i==8:
            data.update({'death_w':item.text})
        i+=1
    return data

def register(request):
    if request.method == 'POST': 
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account create for {username}!')
            return redirect('login')        
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account has been updated ')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'permissions': utilities.get_user_permissions(request.user)
    }
    return render(request,'profile.html', context)


# CHART DATA
class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = {
            'permissions': utilities.get_user_permissions(self.request.user),
            'physical' : get_physical_list(self.request.user.id),
            'news': crawNewsData('https://ncov.moh.gov.vn/en/web/guest/trang-chu'),
            'selected_tab': 'dashboard',
        }
        return context

def get_physical_list(user_id):
    url = 'http://127.0.0.1:8000/api/physical/user/'+str(user_id)
    r = requests.get(url)
    physical = r.json()
    physical_list = physical
    return physical_list
