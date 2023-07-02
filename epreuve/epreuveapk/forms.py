from django import forms

from .models import zipFile

class uploadZipFileForm(forms.ModelForm):
    class Meta:
        model = zipFile
        fields = [
            'filename'
        ]