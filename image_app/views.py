from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Image



def Gallery(request):
    images = Image.objects.all()
    return render(request, "image_app/index.html", {"images": images})



def AddImage(request):
    if request.method == "POST":
        img = Image()
        img.name = request.POST.get('name')
        print(request.POST)
        img.save()
    return HttpResponseRedirect(reverse('gallery'))
