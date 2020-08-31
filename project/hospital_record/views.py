from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib import messages
import requests
from .forms import PostHospitalRecord, PutHospitalRecord
from .serializer import HospitalRecordSerializer
from django.views.generic import TemplateView, DetailView
from project import utilities

#CALL API GET LIST
class GetHospitalRecordList(TemplateView):
    def get_template_names(self):
        return utilities.get_template_names(self.request.user, 'view_hospitalrecordmodel', 'list_hospital_record.html')

    def get_context_data(self, *args, **kwargs):
        group = utilities.get_user_group(self.request.user)
        for gr in group:
            if str(gr)=='Doctor':
                print("okkkkkkkkkkkkkkkkkkkkkkk")
                context = {
                    'selected_tab': 'hospital_record',
                    'permissions': utilities.get_user_permissions(self.request.user),
                    'hospital_record' : get_all_hospital_record(self.request.user.id),
            }
            else:
                print("---------------------------")
                context = {
                    'selected_tab': 'hospital_record',
                    'permissions': utilities.get_user_permissions(self.request.user),
                    'hospital_record' : get_hospital_record_list(self.request.user.id),
            }
            return context

def get_hospital_record_list(user_id):
    url = 'http://127.0.0.1:8000/api/hospital-record/user/'+str(user_id)
    r = requests.get(url)
    hospital_record = r.json()
    hospital_record_list = hospital_record
    return hospital_record_list

def get_all_hospital_record(user_id):
    url = 'http://127.0.0.1:8000/api/hospital-record/'
    r = requests.get(url)
    hospital_record = r.json()
    hospital_record_list = hospital_record
    return hospital_record_list

#CALL API GET FILTER LIST
class FilterHospitalRecordList(TemplateView):
    def get_template_names(self):
        return utilities.get_template_names(self.request.user, 'view_hospitalrecordmodel', 'list_hospital_record.html')

    def get_context_data(self, *args, **kwargs):
        print("--------------")
        context = {
            'selected_tab': 'hospital_record',
            'permissions': utilities.get_user_permissions(self.request.user),
            'hospital_record' : filter_hospital_record_list(self.request.user.id, self.request),
        }
        print(str(self.request)+"=======================")
        return context

def filter_hospital_record_list(user_id, request):
    disease=request.GET.get('disease')
    print(str(disease)+"--------------")
    url = 'http://127.0.0.1:8000/api/hospital-record/filter/{}?disease={}'.format(user_id, disease)
    r = requests.get(url)
    hospital_record = r.json()
    hospital_record_list = hospital_record
    return hospital_record_list

# CALL API POST
@csrf_exempt
def save_hospital_record(request):
    if request.method == "POST" and utilities.is_permission_granted(request.user, 'add_hospitalrecordmodel'):
        h_form = PostHospitalRecord(request.POST)
        if h_form.is_valid():
            hospital = h_form.cleaned_data['hospital']
            disease = h_form.cleaned_data['disease']
            start_time = h_form.cleaned_data['start_time']
            status = h_form.cleaned_data['status']
            user = h_form.cleaned_data['user']
            r = requests.post('http://127.0.0.1:8000/api/hospital-record/', data = {'hospital':hospital,
                                                                                    'disease':disease,
                                                                                    'start_time':start_time,
                                                                                    'status':status,
                                                                                    'user':user.id})
            if r.status_code == 200 or 201:
                data = r.json()
                print(data)
                return redirect('hospital_record_list')
        else:
        # Added else statment
            msg = 'Errors: %s' % h_form.errors.as_text()
            return HttpResponse(msg, status=400)
    else:
        h_form = PostHospitalRecord()

    context =  {
        'selected_tab': 'hospital_record',
        'permissions': utilities.get_user_permissions(request.user),
        'h_form': h_form
    }

    return render(request, utilities.get_template_name(request.user, 'add_hospitalrecordmodel', 'create_hospital_record_form.html'), context)

#CALL API GET DETAIL
class GetHospitalRecordDetail(TemplateView):
    def get_template_names(self):
        return utilities.get_template_names(self.request.user, 'change_hospitalrecordmodel', 'detail_hospital_record.html')

    def get_context_data(self, id, *args, **kwargs):
        context = {
            'selected_tab': 'hospital_record',
            'permissions': utilities.get_user_permissions(self.request.user),
            'hospital_record' : get_hospital_record_detail(id),
        }
        return context

def get_hospital_record_detail(id):
    url = 'http://127.0.0.1:8000/api/hospital-record/'+str(id)
    r = requests.get(url)
    hospital_record = r.json()
    return hospital_record

#CALL API PUT
@csrf_exempt
def update_hospital_record(request, id):
    if request.method == "POST" and utilities.is_permission_granted(request.user, 'change_hospitalrecordmodel'):
        h_form = PutHospitalRecord(request.POST)
        if h_form.is_valid():
            hospital = h_form.cleaned_data['hospital']
            disease = h_form.cleaned_data['disease']
            start_time = h_form.cleaned_data['start_time']
            status = h_form.cleaned_data['status']
            user = h_form.cleaned_data['user']
            r = requests.put('http://127.0.0.1:8000/api/hospital-record/{}/'.format(id), data = {'hospital':hospital,
                                                                                                'disease':disease,
                                                                                                'start_time':start_time,
                                                                                                'status':status,
                                                                                                'user':user.id})
            if r.status_code == 200 or 201:
                data = r.json()
                print(data)
                return redirect('hospital_record_list')
        else:
        # Added else statment
            msg = 'Errors: %s' % h_form.errors.as_text()
            return HttpResponse(msg, status=400)

#CALL API DELETE
@csrf_exempt
def delete_hospital_record(request, id):
    if utilities.is_permission_granted(request.user, 'delete_hospitalrecordmodel'):
        r = requests.delete('http://127.0.0.1:8000/api/hospital-record/{}/'.format(id))

        if r.status_code == 200:
            messages.success(request, f'Delete successfully')
            data = r.json()
            print(data)

    return redirect('hospital_record_list')
