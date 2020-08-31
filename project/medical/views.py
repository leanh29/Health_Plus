from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib import messages
import requests
from .forms import PostMedical, PutMedical
from .serializer import MedicalSerializer
from django.views.generic import TemplateView, DetailView
from project import utilities

#CALL API GET LIST
class GetMedicalList(TemplateView):
    # paginate_by = settings.QUOTES_PER_PAGE
    # context_object_name = 'quotes'
    def get_template_names(self):
        return utilities.get_template_names(self.request.user, 'view_medicalmodel', 'list_medical.html')

    def get_context_data(self, *args, **kwargs):
        page=1
        page = self.request.GET.get('page')

        context = {
            'selected_tab': 'medical',
            'permissions': utilities.get_user_permissions(self.request.user),
            'medical' : get_medical_list(page),
        }
        return context

def get_medical_list(page):
    if page==None: page=1
    url = 'http://127.0.0.1:8000/api/medical/?page={}'.format(page)
    r = requests.get(url)
    medical = r.json()
    medical_list = medical
    print(medical_list)
    return medical_list

class FilterMedicalList(TemplateView):
    # paginate_by = settings.QUOTES_PER_PAGE
    # context_object_name = 'quotes'
    def get_template_names(self):
        return utilities.get_template_names(self.request.user, 'view_medicalmodel', 'list_medical.html')

    def get_context_data(self, *args, **kwargs):

        context = {
            'selected_tab': 'medical',
            'permissions': utilities.get_user_permissions(self.request.user),
            'medical' : filter_all_medical(self.request),
        }
        return context

def filter_all_medical(request):
    name=request.GET.get('name')
    print(str(name)+"--------------")
    url = 'http://127.0.0.1:8000/api/medical/filter?name={}'.format(name)
    r = requests.get(url)
    medical = r.json()
    medical_list = medical
    return medical_list

# CALL API POST
@csrf_exempt
def save_medical(request):
    if request.method == "POST" and utilities.is_permission_granted(request.user, 'add_medicalmodel'):
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

    context =  {
        'selected_tab': 'medical',
        'permissions': utilities.get_user_permissions(request.user),
        'm_form': m_form
    }

    return render(request, utilities.get_template_name(request.user, 'add_medicalmodel', 'create_medical_form.html'), context)

#CALL API GET DETAIL
class GetMedicalDetail(TemplateView):
    def get_template_names(self):
        return utilities.get_template_names(self.request.user, 'change_medicalmodel', 'detail_medical.html')

    def get_context_data(self, id, *args, **kwargs):
        context = {
            'selected_tab': 'medical',
            'permissions': utilities.get_user_permissions(self.request.user),
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
    if request.method == "POST" and utilities.is_permission_granted(request.user, 'change_medicalmodel'):
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
    if utilities.is_permission_granted(request.user, 'delete_medicalmodel'):
        r = requests.delete('http://127.0.0.1:8000/api/medical/{}/'.format(id))

        if r.status_code == 200:
            messages.success(request, f'Delete successfully')
            data = r.json()
            print(data)

    return redirect('medical_list')