from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib import messages
import requests
from .forms import PostReExamination, PutReExamination
from .serializer import ReExeminationSerializer
from django.views.generic import TemplateView, DetailView
from project import utilities

#CALL API GET RE-EXAMINATION LIST
class GetReExaminationList(TemplateView):
    def get_template_names(self):
        return utilities.get_template_names(self.request.user, 'view_reexaminationmodel', 'list_re_examination.html')

    def get_context_data(self, hospital_record_id, *args, **kwargs):
        context = {
            'selected_tab': 'hospital_record',
            'permissions': utilities.get_user_permissions(self.request.user),
            'hospital_record_id': hospital_record_id,
            're_examination' : get_re_examination_list(hospital_record_id),
        }
        return context

def get_re_examination_list(hospital_record_id):
    url = 'http://127.0.0.1:8000/api/re-examination/hospital_record/' + str(hospital_record_id)
    r = requests.get(url)
    re_examination = r.json()
    re_examination_list = re_examination
    return re_examination_list

# CALL API GET MEDICAL LIST OF RE-EXAMINATION
# def get_medical_detail_list(re_examination_id=None):
#     #if re_examination_id:
#     url = 'http://127.0.0.1:8000/api/medical-detail/re-examination/{}/'.format(re_examination_id)
#     # else:
#     #     url = 'http://127.0.0.1:8000/api/medical-detail/re-examination/'

#     return requests.get(url).json()

# CALL API GET MEDICAL LIST 
def get_medical_list(re_examination_id=None):
    # if re_examination_id:
    #     url = 'http://127.0.0.1:8000/api/medical-detail/re-examination/{}/'.format(re_examination_id)
    # else:
    url = 'http://127.0.0.1:8000/api/medical-detail/re-examination/'

    return requests.get(url).json()

# CALL API POST
@csrf_exempt
def save_re_examination(request, hospital_record_id):
    if request.method == "POST" and utilities.is_permission_granted(request.user, 'add_reexaminationmodel'):
        r_form = PostReExamination(request.POST)
        if r_form.is_valid():
            doctor = r_form.cleaned_data['doctor']
            result = r_form.cleaned_data['result']
            date = r_form.cleaned_data['date']
            appointment_date = r_form.cleaned_data['appointment_date']
            r = requests.post('http://127.0.0.1:8000/api/re-examination/hospital_record/{}/'.format(hospital_record_id), data = {'doctor':doctor,
                                                                                    'result':result,
                                                                                    'date':date,
                                                                                    'appointment_date':appointment_date,
                                                                                    'hospital_record':hospital_record_id})
            if r.status_code == 200 or 201:
                data = r.json()
                print(data)
                return redirect('re_examination_list', hospital_record_id=hospital_record_id)
        else:
        # Added else statment
            msg = 'Errors: %s' % r_form.errors.as_text()
            return HttpResponse(msg, status=400)
    else:
        r_form = PostReExamination()

    context =  {
        'selected_tab': 'hospital_record',
        'permissions': utilities.get_user_permissions(request.user),
        'hospital_record_id': hospital_record_id,
        'medical_detail_list': get_medical_detail_list(),
        'r_form': r_form
    }

    return render(request, utilities.get_template_name(request.user, 'add_reexaminationmodel', 'create_re_examination_form.html'), context)

#CALL API PUT
@csrf_exempt
def update_re_examination(request, hospital_record_id, id):
    if request.method == "POST" and utilities.is_permission_granted(request.user, 'change_reexaminationmodel'):
        r_form = PutReExamination(request.POST)

        if r_form.is_valid():
            doctor = r_form.cleaned_data['doctor']
            result = r_form.cleaned_data['result']
            date = r_form.cleaned_data['date']
            appointment_date = r_form.cleaned_data['appointment_date']
            r = requests.put('http://127.0.0.1:8000/api/re-examination/{}/'.format(id), data = {'doctor':doctor,
                                                                                    'result':result,
                                                                                    'date':date,
                                                                                    'appointment_date':appointment_date,
                                                                                    'hospital_record':hospital_record_id})
            if r.status_code == 200 or 201:
                data = r.json()     
                print(data)
                return redirect('re_examination_list', hospital_record_id=hospital_record_id)
        else:
            msg = 'Errors: %s' % r_form.errors.as_text()
            return HttpResponse(msg, status=400)
    else:
        msg = 'Method is not supported'
        return HttpResponse(msg, status=400)

#CALL API DELETE
@csrf_exempt
def delete_re_examination(request, hospital_record_id, id):
    if utilities.is_permission_granted(request.user, 'delete_reexaminationmodel'):
        r = requests.delete('http://127.0.0.1:8000/api/re-examination/{}/'.format(id))

        if r.status_code == 200:
            messages.success(request, f'Delete successfully')
            data = r.json()
            print(data)

    return redirect('re_examination_list', hospital_record_id=hospital_record_id)

#CALL API GET RE-EXAMINATION DETAIL (PRESCRIPTION)
class GetReExaminationDetail(TemplateView):
    def get_template_names(self):
        return utilities.get_template_names(self.request.user, 'view_medicaldetailmodel', 'list_medical_detail.html')

    def get_context_data(self, hospital_record_id, id, *args, **kwargs):
        context = {
            'selected_tab': 'hospital_record',
            'permissions': utilities.get_user_permissions(self.request.user),
            'hospital_record_id': hospital_record_id,
            'medical_detail_list': get_medical_detail_list(id),
        }
        return context

def get_medical_detail_list(re_examination_id=None):
    #if re_examination_id:
    url = 'http://127.0.0.1:8000/api/medical-detail/{}/'.format(re_examination_id)
    # else:
    #     url = 'http://127.0.0.1:8000/api/medical-detail/re-examination/'

    return requests.get(url).json()

def get_re_examination_detail(id):
    url = 'http://127.0.0.1:8000/api/re-examination/'+str(id)
    r = requests.get(url)
    re_examination = r.json()
    print(re_examination)
    return re_examination