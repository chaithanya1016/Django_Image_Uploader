from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from webapp.forms import ImageForm
from django.contrib import messages
from webapp.models import Image

# Create your views here.

def Image_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request, 'Image Uploaded Succesfully')
            form.save()
            return HttpResponseRedirect('/')
    else:
        images = Image.objects.all().order_by('-id')
        form = ImageForm()
    return render(request, 'webapp/imageupload.html', {'images': images, 'form': form })

