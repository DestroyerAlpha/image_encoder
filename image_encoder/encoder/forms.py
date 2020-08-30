from django import forms
from .models import Image

class ImageUploadForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.ClearableFileInput(
        attrs={
            'id': 'upload_file'
        }
    ))
    error_css_class = 'error_msg'
    class Meta:
        model = Image
        fields = [
            'image'
        ]