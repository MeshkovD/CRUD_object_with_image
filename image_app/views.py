from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from .models import SimpleAddPicture
from .forms import SimpleAddPictureForm

def PhotoGallery(request):
    photos = SimpleAddPicture.objects.all()
    form = SimpleAddPictureForm()
    if request.method == 'POST':
        form = SimpleAddPictureForm(request.POST, request.FILES)
        if form.is_valid():
            if 'photo' in request.FILES:
                form.photo = request.FILES['photo']
            form.save(commit=True)
            return HttpResponseRedirect(reverse('photo_gallery'))
        else:
            print(form.errors)
            return render(request, 'image_app/add_simple_picture.html', {'form': form})
    else:
        return render(request, "image_app/photo_gallery.html",{"photos": photos, "form": form})


def picture_page(request, id):
    photo = SimpleAddPicture.objects.get(id__iexact=id)
    return render(request, "image_app/picture_page.html", {'photo': photo})


def picture_delete(request, id):
    try:
        photo = SimpleAddPicture.objects.get(id__iexact=id)
        photo.delete()
        photos = SimpleAddPicture.objects.all()
        form = SimpleAddPictureForm()
        return HttpResponseRedirect(reverse('photo_gallery'))
        # return render(request, "image_app/photo_gallery.html", {"photos": photos, "form": form})
    except SimpleAddPicture.DoesNotExist:
        return HttpResponseNotFound("<h2>Картинка не найдена</h2>")
