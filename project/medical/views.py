from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib import messages
import requests
from .forms import PostMedical, PutMedical
from .serializer import MedicalSerializer
from django.views.generic import TemplateView, DetailView

#CALL API GET LIST
class GetMedicalList(TemplateView):
    template_name = 'list_medical.html'
    def get_context_data(self, *args, **kwargs):
        context = {
            'medical' : get_medical_list(),
        }
        return context

def get_medical_list():
    url = 'http://127.0.0.1:8000/api/medical/'
    r = requests.get(url)
    medical = r.json()
    medical_list = medical
    return medical_list

# CALL API POST
@csrf_exempt
def save_medical(request):
    if request.method == "POST":
        m_form = PostMedical(request.POST)
        if m_form.is_valid():
            name = m_form.cleaned_data['name']
            effect = m_form.cleaned_data['effect']
            r = requests.post('http://127.0.0.1:8000/api/medical/', data = {'name':name, 'effect':effect})
            if r.status_code == 200 or 201:
                data = r.json()
                print(data)
                return redirect('medical_list')
        else:
        # Added else statment
            msg = 'Errors: %s' % m_form.errors.as_text()
            return HttpResponse(msg, status=400)
    else:
        m_form = PostMedical()

    return render(request, 'create_medical_form.html',{'m_form':m_form})

#CALL API GET DETAIL
class GetMedicalDetail(TemplateView):
    template_name = 'detail_medical.html'
    def get_context_data(self, id, *args, **kwargs):
        context = {
            'medical' : get_medical_detail(id),
        }
        return context

def get_medical_detail(id):
    url = 'http://127.0.0.1:8000/api/medical/'+str(id)
    r = requests.get(url)
    medical_record = r.json()
    return medical_record

#CALL API PUT
@csrf_exempt
def update_medical(request, id):
    if request.method == "POST":
        m_form = PutMedical(request.POST)
        if m_form.is_valid():
            name = m_form.cleaned_data['name']
            effect = m_form.cleaned_data['effect']
            r = requests.put('http://127.0.0.1:8000/api/medical/{}/'.format(id), data = {'name':name, 'effect':effect})
            if r.status_code == 200 or 201:
                data = r.json()
                print(data)
                return redirect('medical_list')
        else:
        # Added else statment
            msg = 'Errors: %s' % m_form.errors.as_text()
            return HttpResponse(msg, status=400)

#CALL API DELETE
@csrf_exempt
def delete_medical(request, id):
    r = requests.delete('http://127.0.0.1:8000/api/medical/{}/'.format(id))
    if r.status_code == 200:
        messages.success(request, f'Delete successfully')
        data = r.json()
        print(data)
    return redirect('medical_list')