import glob
import pickle
import numpy as np

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'App_main/home.html')




def heart_disease_detect(request):
    with open('App_main/models/heart_disease_model', 'rb') as f:
        heart_model = pickle.load(f)
    content = {

    }
    if request.method == 'POST':
        age = int(request.POST.get('age'))
        sex = int(request.POST.get('gender'))
        cp = int(request.POST.get('chest_pain'))
        trestbps = int(request.POST.get('blood_pressure'))
        chol = int(request.POST.get('cholesterol'))
        fbs = int(request.POST.get('fasting_bp'))
        restecg = int(request.POST.get('restecg'))
        thalach = int(request.POST.get('maximum_heart_rate'))
        exang = int(request.POST.get('exang'))
        oldpeak = float(request.POST.get('oldpeak'))
        slop = int(request.POST.get('slop'))
        ca = int(request.POST.get('ca'))
        thal = int(request.POST.get('thalassemia'))

        input_data = (age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slop, ca, thal)
        input_data_array = np.asarray(input_data)
        input_shape = input_data_array.reshape(1, -1)
        predict = heart_model.predict(input_shape)
        if predict[0] == 0:
            content['predicted_result'] = 0
        elif predict[0] == 1:
            content['predicted_result'] = 1
        else:
            content['predicted_result'] = 2
    return render(request, 'App_main/heart.html', context=content)


def about(request):
    return render(request, 'App_main/about.html')


def profile(request):
    return render(request, 'App_main/profile.html')