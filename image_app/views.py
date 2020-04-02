from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse, reverse_lazy
from django.views.generic import View, ListView, DeleteView

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

# class PhotoGallery(ListView):
#     model = SimpleAddPicture
#     context_object_name = 'photos'
#     template_name = 'image_app/photo_gallery.html'
#     # paginate_by = 3

    def get_queryset(self):
        qs = SimpleAddPicture.objects.all()
        return qs

    # photos = SimpleAddPicture.objects.all()
    # form = SimpleAddPictureForm()
    # def get(self, request):

# def picture_page(request, id):
#     photo = SimpleAddPicture.objects.get(id__iexact=id)
#     return render(request, "image_app/picture_page.html", {'photo': photo})

class PicturePage(View):
    def get(self, request, id):
        # photo = SimpleAddPicture.objects.get(id__iexact=id)
        photo = get_object_or_404(SimpleAddPicture, id__iexact=id)
        return render(request, "image_app/picture_page.html", {'photo': photo})


# def picture_delete(request, id):
#     try:
#         photo = SimpleAddPicture.objects.get(id__iexact=id)
#         photo.delete()
#         photos = SimpleAddPicture.objects.all()
#         form = SimpleAddPictureForm()
#         return HttpResponseRedirect(reverse('photo_gallery'))
#         # return render(request, "image_app/photo_gallery.html", {"photos": photos, "form": form})
#     except SimpleAddPicture.DoesNotExist:
#         return HttpResponseNotFound("<h2>Картинка не найдена</h2>")

class PictureDelete(View):
    def get(self, request, id):
        pict = SimpleAddPicture.objects.get(id__iexact=id)
        return render(request, 'image_app/photo_delete.html', context={'pict': pict})

    def post(self, request, id):
        pict = SimpleAddPicture.objects.get(id__iexact=id)
        pict.delete()
        return redirect(reverse('photo_gallery'))



def picture_edit(request, id):
    form = SimpleAddPictureForm()
    try:
        photo = SimpleAddPicture.objects.get(id__iexact=id)

        if request.method == "POST":
            photo.title = request.POST.get("title")
            photo.photo = request.FILES.get("photo")
            # photo.photo = request.POST.get
            photo.save()
            return HttpResponseRedirect(reverse('photo_gallery'))
        else:
            return  render(request, 'image_app/picture_edit.html', {"photo": photo, "form": form})
    except SimpleAddPicture.DoesNotExist:
        return HttpResponseNotFound("<h2> Картинка не найдена </h2>")
