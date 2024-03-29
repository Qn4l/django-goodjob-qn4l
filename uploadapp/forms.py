from .models import Uploads, UploadFile
from django import forms


class UploadForm(forms.ModelForm):
    class Meta:
        model = Uploads
        fields = '__all__'


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = '__all__'
