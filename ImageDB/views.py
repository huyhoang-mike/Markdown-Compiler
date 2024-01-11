from django.shortcuts import render
from .models import Image
import base64
import numpy as np
from PIL import Image

# Create your views here.

def index(request):
    # obj = Image.objects.all()
    # context = {
    #     'obj': obj
    # }
    return render(request, 'index.html', {})

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

def show(request):
    if request.method == "POST":
        try:
            image = request.FILES["imagefile"]
            # encode image to base64 string
            image_base64 = base64.b64encode(image.read()).decode("utf-8")
        except:
            # messages.add_message(
            #     request, messages.ERROR, "No image selected or uploaded"
            # )
            return render(request, "show.html")
        # lang = request.POST["language"]
        img = np.array(Image.open(image))
        # text = pytesseract.image_to_string(img, lang=lang)
        # return text to html
        return render(request, "show.html", {"image": image_base64})

    return render(request, "show.html")