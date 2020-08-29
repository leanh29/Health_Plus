from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings
from django.contrib import messages
import requests
from .forms import PostPhysical, PutPhysical
from .serializer import PhysicalSerializer
from django.views.generic import TemplateView, DetailView
from project import utilities

#CALL API GET LIST
class GetPhysicalList(TemplateView):
    def get_template_names(self):
        return utilities.get_template_names(self.request.user, 'view_physicalmodel', 'list_physical.html')

    def get_context_data(self, *args, **kwargs):
        context = {
            'selected_tab': 'physical',
            'permissions': utilities.get_user_permissions(self.request.user),
            'physical' : get_physical_list(self.request.user.id),
        }
        return context

def get_physical_list(user_id):
    url = 'http://127.0.0.1:8000/api/physical/user/'+str(user_id)
    r = requests.get(url)
    physical = r.json()
    physical_list = physical
    return physical_list

#CALL API FILLTER PHYSICAL
class FilterPhysicalList(TemplateView):
    def get_template_names(self):
        return utilities.get_template_names(self.request.user, 'view_physicalmodel', 'list_physical.html')

    def get_context_data(self, *args, **kwargs):
        context = {
            'selected_tab': 'physical',
            'permissions': utilities.get_user_permissions(self.request.user),
            'physical' : filter_physical_list(self.request.user.id, self.request),
        }
        return context

def filter_physical_list(user_id, request):
    height=request.GET.get('height')
    url = 'http://127.0.0.1:8000/api/physical/filter/{}?height={}'.format(user_id, height)
    r = requests.get(url)
    physical = r.json()
    physical_list = physical
    return physical_list

# CALL API POST
@csrf_exempt
def save_physical(request):
    if request.method == "POST" and utilities.is_permission_granted(request.user, 'add_physicalmodel'):
        form = PostPhysical(request.POST)
        if form.is_valid():
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            date = form.cleaned_data['date']
            user = form.cleaned_data['user']
            r = requests.post('http://127.0.0.1:8000/api/physical/', data = {'height':height, 'weight':weight, 'date':date, 'user':user.id})
            if r.status_code == 200 or 201:
                data = r.json()
                print(data)
                return redirect('physical_list')
            else:
                msg = r.json()
                return HttpResponse(msg)
        else:
        # Added else statment
            msg = 'Errors: %s' % form.errors.as_text()
            return HttpResponse(msg, status=400)
    else:
        form = PostPhysical()

    context =  {
        'selected_tab': 'physical',
        'permissions': utilities.get_user_permissions(request.user),
        'form': form
    }

    return render(request, utilities.get_template_name(request.user, 'add_physicalmodel', 'create_form.html'), context)

#CALL API GET DETAIL
class GetPhysicalDetail(TemplateView):
    def get_template_names(self):
        return utilities.get_template_names(self.request.user, 'change_physicalmodel', 'detail_physical.html')

    def get_context_data(self, id, *args, **kwargs):
        context = {
            'selected_tab': 'physical',
            'permissions': utilities.get_user_permissions(self.request.user),
            'physical': get_physical_detail(id)
        }
        return context

def get_physical_detail(id):
    url = 'http://127.0.0.1:8000/api/physical/'+str(id)
    r = requests.get(url)
    physical = r.json()
    print(physical)
    return physical

#CALL API PUT
@csrf_exempt
def update_physical(request, id):
    if request.method == "POST" and utilities.is_permission_granted(request.user, 'change_physicalmodel'):
        form = PutPhysical(request.POST)
        #form = PutPhysical(request.POST,instance=request.physical)
        if form.is_valid():
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            date = form.cleaned_data['date']
            user = form.cleaned_data['user']
            r = requests.put('http://127.0.0.1:8000/api/physical/{}/'.format(id), data = {'height':height, 'weight':weight, 'date':date, 'user':user.id})
            if r.status_code == 200 or 201:
                data = r.json()
                print(data)
                return redirect('physical_list')
        else:
            msg = 'Errors: %s' % form.errors.as_text()
            return HttpResponse(msg, status=400)

#CALL API DELETE
@csrf_exempt
def delete_physical(request, id):
    if utilities.is_permission_granted(request.user, 'delete_physicalmodel'):
        r = requests.delete('http://127.0.0.1:8000/api/physical/{}/'.format(id))

        if r.status_code == 200:
            messages.success(request, f'Delete successfully')
            data = r.json()
            print(data)

    return redirect('physical_list')
