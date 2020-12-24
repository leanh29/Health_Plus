from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, HttpResponse
import requests
from .forms import PostSymptom
from project import utilities
from m_Summarize import get_predict
from django.template.loader import render_to_string
from decimal import  *
from django.http import JsonResponse

# CALL API POST
@csrf_exempt
def save_symptom(request):
    result = 'vvv'
    if request.method == 'POST':
        msg = ''
        form = PostSymptom(request.POST)

        if form.is_valid():
            symptom = form.cleaned_data['symptom']
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']

            conditon = bmi(height, weight)

            new_symptom = symptom + " , " + conditon
            print('input symptom: ',new_symptom)
            # check_format(new_symptom)
            disease = get_predict(new_symptom)
            print('disease: ', disease)
            result='Khoa tổng quát'
            if (disease=='bệnh viêm đường ruột')==True:
                result = 'Khoa tiêu hóa'
            if (disease=='bệnh hạ huyết áp')==True:
                result = 'Khoa tim mạch'

            print("Result", result)
            return JsonResponse({
                'success': True,
                'msg': msg,
                'result': str(result)
            })
        else:
            msg = 'Errors: %s' % form.errors.as_text()
            # return HttpResponse(msg, status=400)
            return JsonResponse({
                'success': False,
                'msg': msg,
                'result': ''
            })
            
    else:
        form = PostSymptom()
        result = '...'

    context = {
        'result': result,
        'form': form
    }

    return render(request, 'index.html', context)


def bmi(height, weight):
    height /= 100.0
    weight += 0.0
    result = ''
    bmi = Decimal(weight)/(Decimal(height) * Decimal(height))
    check_bmi = round(bmi,1)
    if check_bmi < Decimal(18.5):
        result = 'thiếu cân'
    if (check_bmi >= Decimal(18.5) and check_bmi <= Decimal(24.9)):
        result = 'bình thường'
    else:
        result = 'thừa cân'
    return result

def check_format(check_str):
    split_str = check_str.split(",")
    checked_str = ''
    count = 1
    for st in split_str:
        if count == len(split_str):
            checked_str += st.strip()
        else:
            checked_str += st.strip()
            checked_str += " , "
        count += 1
    print(checked_str)
    return checked_str