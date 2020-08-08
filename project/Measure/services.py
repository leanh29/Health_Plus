from django.http import HttpResponse
import requests
import time

def get_measure_list():
    url = 'http://127.0.0.1:8000/api/measure-list/'
    r = requests.get(url)
    measures = r.json()
    measures_list = measures
    return measures_list

def get_measure(pk):
    url = 'http://127.0.0.1:8000/api/measure/'+str(pk) 
    #params = {'year': year, 'author': author}
    r = requests.get(url)
    measures = r.json()
    measures_list = measures
    # for i in range(len(measures)):
    #     measures_list.append(measures[i])
    return measures_list