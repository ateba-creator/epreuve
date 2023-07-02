from django.db import models

# Create your models here.

class Zipepreuve(models.Model):
    filename = models.FileField(upload_to='zipfile')
    hours = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = ('Zipepreuve')
        verbose_name_plural = ('Zipepreuves')
        
    

class Fichierzip(models.Model):
    file=models.FileField(upload_to='zipfile')
    date = models.DateTimeField( auto_now_add=True)

    class Meta:
        ordering=['-date']

    def __str__(self):
        return str(self.date)
    

# class Fichierzip(models.Model):
#     date = models.DateTimeField(auto_now_add=True)
#     file = models.FileField(upload_to='zipfile')
#     nom_doc = models.CharField(max_length=50)