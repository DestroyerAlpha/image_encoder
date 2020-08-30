from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import ImageUploadForm
from .models import Image
import hashlib, json, base64, os
from .encryption import encrypt


def upload(request):
    if request.method == 'POST':
        #Form received via post
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            #image file received via post
            img = form.cleaned_data.get("image")
            #Image Obj created
            obj = Image.objects.create(image = img)
            #Object saved in database and filesystems
            obj.save()
            #Use the image id of the object for displaying the JSON Result
            imgid = obj.id
            return redirect('output', imgid)
        else:
            print(form.errors)
    else:
        form = ImageUploadForm(request.POST)
    return render(request, 'encoder/index.html', {'form': form})

def result(request, imgid):
    img = Image.objects.get(id=imgid)
    #open image saved in the filesystems
    with open(img.image.url, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    md5 = hashlib.md5(encoded_string)
    #remove imaage from the database
    img.delete()
    #remove image from the filesystems
    os.remove(img.image.url)

    ##Using MD5 Hexsum as the password for the datetime AES
    aes = encrypt(md5.hexdigest())
    context = {'base64': encoded_string.decode('utf-8'), 'md5_hash': md5.hexdigest(), 'aes':aes}
    # context = json.dumps(context)
    return JsonResponse(context, json_dumps_params={'indent': 2})