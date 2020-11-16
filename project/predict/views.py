from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, HttpResponse
import requests
from .forms import PostSymptom
from project import utilities
from m_Summarize import get_predict


# CALL API POST
@csrf_exempt
def save_symptom(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PostSymptom(request.POST)
        # check whether it's valid:
        if form.is_valid():
            symptom = form.cleaned_data['symptom']
            get_predict(symptom)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # Added else statement
            # msg = 'Errors: %s' % form.errors.as_text()
            return HttpResponse('msg', status=400)

        # if a GET (or any other method) we'll create a blank form
    else:
        form = PostSymptom()

    return render(request, 'symptom_form.html', {'form': form})



