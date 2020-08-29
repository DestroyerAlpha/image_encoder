from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import Image
import base64

# Create your views here.
def upload(request):
    if request.method == 'POST':
        print('received')
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.cleaned_data.get("image") 
            print('success')
            obj = Image.objects.create(image = img)
            obj.save()
            imgid = obj.id
            return redirect('output', imgid)
        print('not valid')
    else:
        form = ImageUploadForm(request.POST)
    return render(request, 'encoder/index.html', {'form': form})

def result(request, imgid):
    image = Image.objects.get(id=imgid)
    with open(image.image.url, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    context = {'base64': encoded_string}
    return render(request, 'encoder/output.html', context)