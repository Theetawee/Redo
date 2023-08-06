from django.shortcuts import render
from accounts.decorators import verified_email_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
import os
from pathlib import Path



@login_required
@verified_email_required
def homepage(request):
    return render(request,'main/index.html' )



def service_worker(request):
    BASE_DIR = Path(__file__).resolve().parent.parent
    path=os.path.join(BASE_DIR,'templates','serviceWorker.js')
    response=HttpResponse(open(path).read(),content_type='application/javascript')
    return response

def manifest(request):
    return render(request, 'manifest.json', content_type='application/json')
    
def offline(request):
    return render(request,'offline.html' )   



def custom_404_view(request,exception):
    return render(request, 'main/error.html', status=404)

def custom_500_view(request):
    return render(request, 'main/505.html', status=500)
