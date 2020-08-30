from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import ImageUploadForm
from .models import Image
import hashlib, json, base64, os
from django.core.exceptions import ValidationError
from .encryption import encrypt


def file_size(value): # add this to some file where you can import it from
    limit = 20 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 20 MB.')

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
        else:
            print(form.errors)
    else:
        form = ImageUploadForm(request.POST)
    return render(request, 'encoder/index.html', {'form': form})

def result(request, imgid):
    img = Image.objects.get(id=imgid)
    print(img.image)
    with open(img.image.url, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    md5 = hashlib.md5(encoded_string)
    img.delete()
    os.remove(img.image.url)
    ##Using MD5 Hexsum as the password for the datetime AES
    aes = encrypt(md5.hexdigest())
    context = {'base64': encoded_string.decode('utf-8'), 'md5_hash': md5.hexdigest(), 'aes':aes['cipher_text']}
    # context = json.dumps(context)
    return JsonResponse(context, json_dumps_params={'indent': 2})