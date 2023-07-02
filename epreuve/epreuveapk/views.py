from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.views.generic.edit import FormView

# Create your views here.
import os,zipfile
from .models import Zipepreuve,Fichierzip

def index(request):
    return render(request,'courses.html')


def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'pages/dashboard.html')
    else:
        return redirect('login')
    
def addEpreuve(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            file = request.POST.get('file')
            print(file)
            path = file             
            root,extension = os.path.splitext(path)
            print(extension)
            if extension =='.zip':
                save_file = Zipepreuve.objects.create(filename=file)
                save_file.save()
                print('ok')
            else:
                print('nn')
        return render(request,'pages/epreuves.html')
    else:
        return redirect('compte')

def home(request):
    images=Fichierzip.objects.all()
    context={
        'images':images
    }
    return render(request, 'pages/form.html', context)

def file_upload(request):
    if request.method == 'POST':
        my_file=request.FILES.get('file')
        fileobj=Fichierzip.objects.create(file=my_file)
        print(fileobj)
        fileobj.save()
    return render(request,'pages/form.html')
    
    

    