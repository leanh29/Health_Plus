from django.urls import path
from predict.views import save_symptom

urlpatterns = [
    path('create/', save_symptom, name='create_predict'),
]