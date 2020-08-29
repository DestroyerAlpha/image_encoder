from django import forms

from .models import Image

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = [
            'image'
        ]
    def __init__(self, *args, **kwargs):
        super(ImageUploadForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False