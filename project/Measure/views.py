from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from . import services
from .services import get_measure_list, get_measure
from .forms import MeasureCreationForm, MeasureUpdateForm
from django.views.decorators.csrf import csrf_exempt
import requests

class GetMeasureList(TemplateView):
    template_name = 'measure_list.html'
    def get_context_data(self, *args, **kwargs):
        context = {
            'measures' : get_measure_list(),
        }
        return context

class GetMeasure(TemplateView):
    template_name = 'measure.html'
    def get_context_data(self,id, *args, **kwargs):
        context = {
            'measure' : get_measure(id),
        }
        return context

# class CreateMeasure(TemplateView):
#     template_name = 'create.html'
#     def get_context_data(self,request, *args, **kwargs):
#         context = {
#             'measure' : create_measure(request),
#         }
#         return context

# class MeasureCreateView(CreateView):
#     model = Measure    
#     fields = ['chieucao', 'cannang']
#     url = 'http://127.0.0.1:8000/api/measure-list/'
#     chieucao = request.POST.get('chieucao')
#     cannang = request.POST.get('cannang')
#     r = requests.post(url, data=request.POST)
#     if r.status_code == 201:
#         data = r.json()
#         print(data)
#         return HttpResponse(r.text)
@csrf_exempt
def create_measure(request):
    if request.method == 'POST': 
        form = MeasureCreationForm()
        url = 'http://127.0.0.1:8000/api/measure-list/'
        chieucao = request.POST.get('chieucao')
        cannang = request.POST.get('cannang')
        r = requests.post(url, data=request.POST)
        if r.status_code == 201:
            data = r.json()
            print(data)
    else:
        form = MeasureCreationForm()
    return render(request, 'create.html', {'form':form})

def get_measure(pk):
    url = 'http://127.0.0.1:8000/api/measure/'+str(pk) 
    #params = {'year': year, 'author': author}
    r = requests.get(url)
    measures = r.json()
    measures_list = measures
    # for i in range(len(measures)):
    #     measures_list.append(measures[i])
    return measures_list

@csrf_exempt
def update_measure(request):
    if request.method == 'POST': 
        form = MeasureUpdateForm()
        url = 'http://127.0.0.1:8000/api/measure/1'
        chieucao = request.POST.get('chieucao')
        cannang = request.POST.get('cannang')
        r = requests.post(url, data=request.POST)
        if r.status_code == 201:
            data = r.json()
            print(data)
    else:
        form = MeasureUpdateForm()
    return render(request, 'create.html', {'form':form})

    if request.method == 'POST':
        form = MeasureUpdateForm()
        url = 'http://127.0.0.1:8000/api/measure/1'
        chieucao = request.POST.get('chieucao')
        cannang = request.POST.get('cannang')
        r = requests.post(url, data=request.POST)
        if r.status_code == 201:
            data = r.json()
            print(data)
    else:
        form = MeasureUpdateForm()
    return render(request, 'create.html', {'form':form})