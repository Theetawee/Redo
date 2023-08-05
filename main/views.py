from django.shortcuts import render
from accounts.decorators import verified_email_required

# Create your views here.

@verified_email_required
def homepage(request):
    return render(request,'main/index.html' )