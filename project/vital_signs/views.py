from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib import messages
import requests
from .forms import PostVitalSigns, PutVitalSigns
from .serializer import VitalSignsSerializer
from django.views.generic import TemplateView, DetailView
from project import utilities
import dateutil.parser

#CALL API GET LIST
class GetVitalSignsList(TemplateView):
    def get_template_names(self):
        return utilities.get_template_names(self.request.user, 'view_vitalsignsmodel', 'list_vital_signs.html')

    def get_context_data(self, *args, **kwargs):
        group = utilities.get_user_group(self.request.user)
        for gr in group:
            if str(gr)=='Doctor':
                context = {
                    'selected_tab': 'vital_signs',
                    'permissions': utilities.get_user_permissions(self.request.user),
                    'vital_signs' : get_all_vital_signs(),
            }
            else:
                context = {
                    'selected_tab': 'vital_signs',
                    'permissions': utilities.get_user_permissions(self.request.user),
                    'vital_signs' : get_vital_signs_list(self.request.user.id),
            }
            return context
        # context = {
        #     'selected_tab': 'vital_signs',
        #     'permissions': utilities.get_user_permissions(self.request.user),
        #     'vital_signs' : get_vital_signs_list(self.request.user.id),
        # }
            # return context

def get_vital_signs_list(user_id):
    url = 'http://127.0.0.1:8000/api/vital-signs/user/'+str(user_id)
    r = requests.get(url)
    vital_signs = r.json()
    vital_signs_list = vital_signs

    for vital_signs in vital_signs_list['results']:
        vital_signs['time'] = dateutil.parser.parse(vital_signs['time']).strftime("%Y-%m-%d %H:%M")

    return vital_signs_list

def get_all_vital_signs():
    url = 'http://127.0.0.1:8000/api/vital-signs/'
    r = requests.get(url)
    vital_signs = r.json()
    vital_signs_list = vital_signs

    for vital_signs in vital_signs_list['results']:
        vital_signs['time'] = dateutil.parser.parse(vital_signs['time']).strftime("%Y-%m-%d %H:%M")

    return vital_signs_list

# CALL API POST
@csrf_exempt
def save_vital_signs(request):
    if request.method == "POST" and utilities.is_permission_granted(request.user, 'add_vitalsignsmodel'):
        v_form = PostVitalSigns(request.POST)
        if v_form.is_valid():
            temperature = v_form.cleaned_data['temperature']
            bool_pressure = v_form.cleaned_data['bool_pressure']
            heartbeat = v_form.cleaned_data['heartbeat']
            breathing = v_form.cleaned_data['breathing']
            user = v_form.cleaned_data['user']
            r = requests.post('http://127.0.0.1:8000/api/vital-signs/', data = {'temperature':temperature, 
                                                                                'bool_pressure':bool_pressure, 
                                                                                'heartbeat':heartbeat, 
                                                                                'breathing':breathing,
                                                                                'user':user.id})
            if r.status_code == 200 or 201:
                data = r.json()
                print(data)
                return redirect('vital_signs_list')
        else:
        # Added else statment
            msg = 'Errors: %s' % v_form.errors.as_text()
            return HttpResponse(msg, status=400)
    else:
        v_form = PostVitalSigns()

    context =  {
        'selected_tab': 'vital_signs',
        'permissions': utilities.get_user_permissions(request.user),
        'v_form': v_form
    }

    return render(request, utilities.get_template_name(request.user, 'add_vitalsignsmodel', 'create_vital_signs_form.html'), context)

#CALL API GET DETAIL
class GetVitalSignsDetail(TemplateView):
    def get_template_names(self):
        return utilities.get_template_names(self.request.user, 'change_vitalsignsmodel', 'detail_vital_signs.html')

    def get_context_data(self, id, *args, **kwargs):
        context = {
            'selected_tab': 'vital_signs',
            'permissions': utilities.get_user_permissions(self.request.user),
            'vital_signs' : get_vital_signs_detail(id),
        }
        return context

def get_vital_signs_detail(id):
    url = 'http://127.0.0.1:8000/api/vital-signs/'+str(id)
    r = requests.get(url)
    vital_signs = r.json()
    return vital_signs

#CALL API PUT
@csrf_exempt
def update_vital_signs(request, id):
    if request.method == "POST" and utilities.is_permission_granted(request.user, 'change_vitalsignsmodel'):
        v_form = PutVitalSigns(request.POST)
        if v_form.is_valid():
            temperature = v_form.cleaned_data['temperature']
            bool_pressure = v_form.cleaned_data['bool_pressure']
            heartbeat = v_form.cleaned_data['heartbeat']
            breathing = v_form.cleaned_data['breathing']
            user = v_form.cleaned_data['user']
            print('http://127.0.0.1:8000/api/vital-signs/{}/'.format(id))
            r = requests.put('http://127.0.0.1:8000/api/vital-signs/{}/'.format(id), data = {'temperature':temperature, 
                                                                                            'bool_pressure':bool_pressure, 
                                                                                            'heartbeat':heartbeat, 
                                                                                            'breathing':breathing,
                                                                                            'user':user.id})
            if r.status_code == 200 or 201:
                data = r.json()
                print(data)
                return redirect('vital_signs_list')
        else:
        # Added else statment
            msg = 'Errors: %s' % v_form.errors.as_text()
            return HttpResponse(msg, status=400)

#CALL API DELETE
@csrf_exempt
def delete_vital(request, id):
    if utilities.is_permission_granted(request.user, 'delete_vitalsignsmodel'):
        r = requests.delete('http://127.0.0.1:8000/api/vital-signs/{}/'.format(id))

        if r.status_code == 200:
            messages.success(request, f'Delete successfully')
            data = r.json()
            print(data)

    return redirect('vital_signs_list')
