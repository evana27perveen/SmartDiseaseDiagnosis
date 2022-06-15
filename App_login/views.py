from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, reverse, HttpResponseRedirect
from .forms import SignupForm, ProfileForm
from django.contrib import messages


def signup(request):
    form1 = SignupForm()
    form2 = ProfileForm()
    if request.method == 'POST':
        form1 = SignupForm(request.POST)
        form2 = ProfileForm(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            this_user = form1.save()
            this_profile = form2.save(commit=False)
            this_profile.user = this_user
            this_profile.save()
            return HttpResponseRedirect(reverse('home'))
    content = {
        'form1': form1,
        'form2': form2
    }
    return render(request, "App_login/signup.html", context=content)


def login_sys(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('App_main:home'))
    diction = {'form': form}
    return render(request, 'App_login/login.html', context=diction)


def logout_sys(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
