from django.shortcuts import render

def handleError(request,exception):
    return render(request,'main/error.html' )