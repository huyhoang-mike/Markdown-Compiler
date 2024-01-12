from django.shortcuts import render
from .models import Image
import base64
import numpy as np
from PIL import Image
import os
import cv2
# Create your views here.

# def index(request):
#     # obj = Image.objects.all()
#     # context = {
#     #     'obj': obj
#     # }
#     return render(request, 'index.html', {})

# def show(request):
#     if request.method == 'POST':
#         img = request.FILES.

#         # if image_file:
#         #     # Handle the image file here
#         #     pass
#         # else:
#         #     print("No image file in request.")

#     context = {
#         'img': img,
#     }
#     return render(request, 'show.html', context)

# def show(request):
#     if request.method == "POST":
#         try:
#             image = request.FILES["imagefile"]
#             # encode image to base64 string
#             image_base64 = base64.b64encode(image.read()).decode("utf-8")
#         except:
#             # messages.add_message(
#             #     request, messages.ERROR, "No image selected or uploaded"
#             # )
#             return render(request, "show.html")
#         # lang = request.POST["language"]
#         img = np.array(Image.open(image))
#         # text = pytesseract.image_to_string(img, lang=lang)
#         # return text to html
#         return render(request, "show.html", {"image": image_base64})

#     return render(request, "show.html")

import numpy as np
from django.conf import settings
from django.core.files.storage import default_storage
from django.shortcuts import render
from matplotlib.image import imread

def index(request):
    if request.method == "POST":
        file = request.FILES["imageFile"]
        file_name = default_storage.save(file.name, file)
        file_url = default_storage.path(file_name)
        dir = os.path.join('.','media')
        for file in os.listdir(dir):
            img = cv2.imread(os.path.join('.','media', file))
            arr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        context = {
        'file_name': file_name,
        'file_url': file_url,
        'dir': dir,
        'arr': arr,
        }
        return render(request, "index.html", context)
    else:
        return render(request, "index.html")
    return render(request, "index.html")