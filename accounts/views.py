from django.shortcuts import redirect, render
from .forms import RegForm
from .models import Account
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from .utils import send_activation_email,generate_token
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth.decorators import login_required



# Create your views here.



def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username_or_email, password=password)
                
            if user is not None:
                login(request, user)
                if not user.verified_email:
                    return redirect('verify_email')
            
                return redirect('home')
    else:
        form = AuthenticationForm(request=request)

    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)





def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.backend = 'accounts.backends.EmailOrUsernameModelBackend'
            login(request, user)
            if not user.verified_email:
                return redirect('verify_email')
            return redirect('home')
    
    else:
        form = RegForm()
    
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)



@login_required
def verify_email(request):
    if request.user.verified_email:
        messages.error(request, 'You have already verified your email.')
        return redirect('home')
    send_activation_email(request.user,request)
    messages.success(request, 'Verification email sent successfully. Please check your inbox.')
    return render(request,'accounts/verify_email.html' )


def logout_user(request):
    logout(request)
    return redirect('login')


def activate_user(request,uidb64,token):
    try:
        uid=force_str(urlsafe_base64_decode(uidb64))
        user=Account.objects.get(pk=uid)
    except:
        user=None
    if user and generate_token.check_token(user,token):
        user.verified_email=True
        user.save()
        messages.success(request,'Email verified successfully')
        return redirect('home')
    
    return render(request,'accounts/verification_failed.html',{"user":user})

