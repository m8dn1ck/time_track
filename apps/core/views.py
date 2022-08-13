from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

#
#import models
from apps.userprofile.models import Userprofile


# Create your views here.
def frontpage(request):
    return render(request, 'core/frontpage.html')
def privacy(request):
    return render(request, 'core/privacy.html')
def information(request):
    return render(request, 'core/information.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.email = user.username
            user.save()

            userprofile = Userprofile.objects.create(user=user)

            login(request, user)

            return redirect('frontpage')

    else:
        form = UserCreationForm()
    
    return render(request, 'core/signup.html', {'form':form})
