from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib import messages
import requests
from .forms import PostVitalSigns, PutVitalSigns
from .serializer import VitalSignsSerializer
from django.views.generic import TemplateView, DetailView

#CALL API GET LIST
class GetVitalSignsList(TemplateView):
    template_name = 'list_vital_signs.html'
    def get_context_data(self, *args, **kwargs):
        context = {
            'vital_signs' : get_vital_signs_list(),
        }
        return context

def get_vital_signs_list():
    url = 'http://127.0.0.1:8000/api/vital-signs/'
    r = requests.get(url)
    vital_signs = r.json()
    vital_signs_list = vital_signs
    return vital_signs_list

# CALL API POST
@csrf_exempt
def save_vital_signs(request):
    if request.method == "POST":
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

    return render(request, 'create_vital_signs_form.html',{'v_form':v_form})

#CALL API GET DETAIL
class GetVitalSignsDetail(TemplateView):
    template_name = 'detail_vital_signs.html'
    def get_context_data(self, id, *args, **kwargs):
        context = {
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
    if request.method == "POST":
        v_form = PutVitalSigns(request.POST)
        #form = PutPhysical(request.POST,instance=request.physical)
        if v_form.is_valid():
            temperature = v_form.cleaned_data['temperature']
            bool_pressure = v_form.cleaned_data['bool_pressure']
            heartbeat = v_form.cleaned_data['heartbeat']
            breathing = v_form.cleaned_data['breathing']
            user = v_form.cleaned_data['user']
            # print(height)
            # print(weight)
            # print(user)
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
    r = requests.delete('http://127.0.0.1:8000/api/vital-signs/{}/'.format(id))
    if r.status_code == 200:
        messages.success(request, f'Delete successfully')
        data = r.json()
        print(data)
    return redirect('vital_signs_list')
    #return render(request, 'list_physical.html')