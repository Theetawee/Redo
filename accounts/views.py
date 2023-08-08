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
from django.utils import timezone
from datetime import datetime, timedelta
from django.conf import settings



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
                destination=request.GET.get('next')
                if destination:
                    return redirect(destination)
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
            destination=request.GET.get('next')
            if destination:
                return redirect(destination)
                
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

    cooldown_seconds = getattr(settings, 'VERIFY_EMAIL_COOLDOWN_SECONDS', 300)
    last_email_sent_time_str = request.session.get('last_email_sent_time')

    if last_email_sent_time_str:
        last_email_sent_time = datetime.fromisoformat(last_email_sent_time_str)
        time_elapsed = timezone.now() - last_email_sent_time
        if time_elapsed.total_seconds() < cooldown_seconds:
            wait_time = timedelta(seconds=cooldown_seconds) - time_elapsed
            minutes, seconds = divmod(wait_time.seconds, 60)
            messages.warning(request, f'Please wait {minutes} minutes and {seconds} seconds before resending the verification email.')
            return render(request,'accounts/verify_email.html')
    
    send_activation_email(request.user, request)

    # Store the current time as a string in ISO format
    request.session['last_email_sent_time'] = timezone.now().isoformat()

    messages.success(request, 'Verification email sent successfully. Please check your inbox.')
    return render(request, 'accounts/verify_email.html')





def logout_user(request):
    if request.POST:
        logout(request)
        return redirect('login')
    return render(request,'accounts/logout.html')


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

def reset_password(request):
    return render(request,'accounts/password_reset',name='reset')

def profile_view(request,slug):
    try:
        account=Account.objects.get(slug=slug)
    except:
        messages.error(request,'Account not found')
        return redirect('home')
    context={
        'account':account
    }
    return render(request,'accounts/profile.html',context)