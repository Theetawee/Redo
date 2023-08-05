from django.shortcuts import render
from accounts.decorators import verified_email_required
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
@verified_email_required
def homepage(request):
    return render(request,'main/index.html' )