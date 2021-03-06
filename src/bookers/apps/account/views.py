from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import authenticate, login
from .forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,
                                username=data['username'],
                                password=data['password'])

            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated Users')
                return HttpResponse('Disabled Account')
            return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
        return render(request, 'account/login.html', {'form':form})


# Create your views here.
