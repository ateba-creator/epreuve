from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.views.generic.edit import FormView
from django.contrib import messages

# Create your views here.
import os,zipfile
from .models import zipFile
from django.core.files.storage import FileSystemStorage

def index(request):
    return render(request,'courses.html')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'pages/dashboard.html')
    else:
        # return redirect('login')
        return render(request,'pages/dashboard.html')


def checkFileExist(filename):
    for file in zipFile.objects.all():
        if str(file.filename) == filename:
            print("file exist")
            return True
    return False
    
def addEpreuve(request):
    if request.method == 'POST' and request.FILES['file']:
        myfile = request.FILES['file']
        
        if(checkFileExist('zip_files/'+ str(myfile))):
            messages.warning(request,"L'epreuve "+str(myfile)+" existe deja dans la base de donnee")
            
        else:
            try:
                newFile = zipFile.objects.create(filename=myfile)
                newFile.save()
                messages.success(request,"Epreuve ajoutee avec succes !")
            
            except Exception as e:
                messages.error(request,e)

    epreuves = zipFile.objects.all()

    context = {
        'epreuves':epreuves,
    }
    return render(request,'pages/epreuves.html',context)


def home(request):
    images=zipFile.objects.all()
    context={
        'images':images
    }
    return render(request, 'pages/form.html', context)

def file_upload(request):
    if request.method == 'POST':
        my_file=request.FILES.get('file')
        fileobj=zipFile.objects.create(file=my_file)
        print(fileobj)
        fileobj.save()
    return render(request,'pages/form.html')
    

def deletePaper(request,id):
    newFile = zipFile.objects.get(id=id)
    newFile.delete()
    messages.success(request,"Epreuve suprimmee avec succes !")

    return redirect('addEpreuve')

    