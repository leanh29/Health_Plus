from django.shortcuts import render, redirect
from django.conf import settings
import requests
from .forms import PostPhysical
from .serializer import PhysicalSerializer
from django.views.generic import TemplateView, CreateView

def save_physical(request):

    if request.method == "POST":
        form = PostPhysical(request.POST)
        if form.is_valid():
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            #r = requests.get('http://127.0.0.1:8000/api/physical/ + '&height=' + height' + '&weight=' + weight)
            r = requests.post('http://127.0.0.1:8000/api/physical/', data = {'height':height, 'weight':weight})
            if r.status_code == 200:
                data = r.json()
                print(data)
            # json = '''{
            #                 "height":1.44444444,
            #                 "weight":2.24444444442
            #             }'''
            # # height = r.json()('height')
            # # weight = r.json()('weight')
            # a = r.json()
            # # hieucao = request.POST.get('height')
            # # cannang = request.POST.get('weight')
            # print(height, weight)
            return redirect('physical_list')
    else:
        form = PostPhysical()

    return render(request, 'form.html',{'form':form})

class GetPhysicalList(TemplateView):
    template_name = 'physical.html'
    def get_context_data(self, *args, **kwargs):
        context = {
            'physical' : get_physical_list(),
        }
        return context

def get_physical_list():
    url = 'http://127.0.0.1:8000/api/physical/'
    #params = {'year': year, 'author': author}
    r = requests.get(url)
    physical = r.json()
    physical_list = physical
    #measures_list = measures
    # for i in range(len(measures)):
    #     measures_list.append(measures[i])
    return physical_list