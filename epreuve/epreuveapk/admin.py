from django.contrib import admin


# Register your models here.
from .models import Zipepreuve,Fichierzip
class AdminZipepreuve(admin.ModelAdmin):
    list_display = ('filename','hours')

class AdminImage(admin.ModelAdmin):
    list_display = ('file','date')
    
class AdminFichierzip(admin.ModelAdmin):
    list_display = ('file','date')    
    
    
admin.site.register(Zipepreuve,AdminZipepreuve)
