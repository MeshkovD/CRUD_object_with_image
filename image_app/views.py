from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse, reverse_lazy
from django.views.generic import View, ListView, DeleteView

from .models import SimpleAddPicture
from .forms import SimpleAddPictureForm


class PictureCreate(View):
    def get(self, request):
        form = SimpleAddPictureForm()
        return render(request, 'image_app/picture_create.html', context={'form': form})

    def post(self, request):
        bound_form = SimpleAddPictureForm(request.POST, request.FILES)

        if bound_form.is_valid():
            new_picture = bound_form.save()
            return redirect('photo_gallery')
        return render(request, 'image_app/picture_create.html', context={'form': bound_form})


class PhotoGallery(ListView):
    model = SimpleAddPicture
    context_object_name = 'photos'
    template_name = 'image_app/photo_gallery.html'
    # paginate_by = 3

    def get_queryset(self):
        qs = SimpleAddPicture.objects.all()
        return qs


class PicturePage(View):
    def get(self, request, id):
        photo = get_object_or_404(SimpleAddPicture, id__iexact=id)
        return render(request, "image_app/picture_page.html", {'photo': photo})


class PictureUpdate(View):
    def get(self, request, id):
        picture = get_object_or_404(SimpleAddPicture, id__iexact=id)
        bound_form = SimpleAddPictureForm(instance=picture)
        return  render(request, 'image_app/picture_update.html', context={'form': bound_form, 'picture': picture})

    def post(self, request, id):
        picture = SimpleAddPicture.objects.get(id__iexact=id)
        bound_form = SimpleAddPictureForm(request.POST, request.FILES, instance=picture)
        if bound_form.is_valid():
            new_picture = bound_form.save()
            return redirect('photo_gallery')
        return render(request, 'image_app/picture_update.html', context={'form': bound_form, 'picture': picture})


class PictureDelete(View):
    def get(self, request, id):
        pict = get_object_or_404(SimpleAddPicture, id__iexact=id)
        return render(request, 'image_app/photo_delete.html', context={'pict': pict})

    def post(self, request, id):
        pict = SimpleAddPicture.objects.get(id__iexact=id)
        pict.delete()
        return redirect(reverse('photo_gallery'))
