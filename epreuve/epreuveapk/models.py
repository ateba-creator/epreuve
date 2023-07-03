from django.db import models
import os
from epreuve import settings
# Create your models here.


class zipFile(models.Model):
    filename=models.FileField(upload_to='zip_files',unique=True)
    date = models.DateTimeField( auto_now_add=True)
    is_valid = models.BooleanField(default=False)
    
    class Meta:
        ordering=['-date']

    def __str__(self):
        return str(self.filename) + str(self.date)
    
    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, str(self.filename)))
        super(zipFile,self).delete(*args,**kwargs)
    