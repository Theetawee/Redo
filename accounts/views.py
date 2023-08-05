from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def login_view(request):
    return render(request,'accounts/login.html')

def signup_view(request):
    form=UserCreationForm()
    context={
        'form':form
    }
    return render(request,'accounts/signup.html',context)