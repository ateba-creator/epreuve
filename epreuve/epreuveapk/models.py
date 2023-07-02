from django.db import models

# Create your models here.

# class FichierZip(models.Model):
#     file=models.FileField(upload_to='zipfile')
#     date = models.DateTimeField( auto_now_add=True)

#     class Meta:
#         ordering=['-date']

#     def __str__(self):
#         return str(self.date)
    

class zipFile(models.Model):
    filename=models.FileField(upload_to='zip_files',unique=True)
    date = models.DateTimeField( auto_now_add=True)
    is_valid = models.BooleanField(default=False)
    
    class Meta:
        ordering=['-date']

    def __str__(self):
        return str(self.date)
    
    
# class Fichierzip(models.Model):
#     date = models.DateTimeField(auto_now_add=True)
#     file = models.FileField(upload_to='zipfile')
#     nom_doc = models.CharField(max_length=50)