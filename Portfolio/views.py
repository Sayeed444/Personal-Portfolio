from django.shortcuts import render,HttpResponse
from django.http import FileResponse, Http404
from .models import Project
import webbrowser
# Create your views here.


def portfolio(request):
    project = Project.objects.all()
    context ={
        'projects':project,
    }
    return render(request,'portfolio/home.html',context)


def pdf(request):
    webbrowser.open_new(r'.\static\portfolio\Sayeed.pdf')
    return render(request,'portfolio/pdf.html')
