from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, HttpResponse
import requests
from .forms import PostSymptom
from project import utilities
from m_Summarize import get_predict
from django.template.loader import render_to_string


# CALL API POST
@csrf_exempt
def save_symptom(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PostSymptom(request.POST)
        # check whether it's valid:
        if form.is_valid():
            symptom = form.cleaned_data['symptom']
            result = get_predict(symptom)
            print('11111111111111111111111', result)
            # msg = 'Errors: %s' % form.errors.as_text()
            # return HttpResponse(result, status=200)
            # return HttpResponse(result)
            rendered = render_to_string('symptom_form.html', {'result': result})
            return HttpResponse(rendered)
        else:
            msg = 'Errors: %s' % form.errors.as_text()
            print('===========================')
            return HttpResponse(msg, status=400)
        # if a GET (or any other method) we'll create a blank form
    else:
        form = PostSymptom()
        result = '...'

    context = {
        'result': result,
        'form': form
    }

    return render(request, 'symptom_form.html', context)



