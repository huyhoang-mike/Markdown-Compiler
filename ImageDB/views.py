from django.shortcuts import render
from .models import Image
import base64
import numpy as np
import pandas as pd 
import os
import cv2

from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL

def explore(request):
    df = pd.read_csv(os.path.join('.','notebooks', 'df_list.csv'))
    result = df.to_html()
    return render(request, 'explore.html', {'result': result, 'df': df})


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

        # Disable scientific notation for clarity
        np.set_printoptions(suppress=True)
        # Load the model
        model = load_model("keras_model.h5", compile=False)
        # Load the labels
        class_names = open("labels.txt", "r").readlines()
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        for file in os.listdir(dir):
            img_file = os.path.join('.','media', file)
            # Replace this with the path to your image
            image = Image.open(img_file).convert("RGB")
            # resizing the image to be at least 224x224 and then cropping from the center
            size = (224, 224)
            image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
            # turn the image into a numpy array
            image_array = np.asarray(image)
            # Normalize the image
            normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
            # Load the image into the array
            data[0] = normalized_image_array
            # Predicts the model
            prediction = model.predict(data)
            index = np.argmax(prediction)
            class_name = class_names[index]
            Class = class_name[2:]
        context = {
        'file_name': file_name,
        'file_url': file_url,
        'dir': dir,
        'Class': Class,
        }
        return render(request, "index.html", context)
    else:
        return render(request, "index.html")
    return render(request, "index.html")