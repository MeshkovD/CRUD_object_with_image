from django.urls import path
from .views import PhotoGallery

urlpatterns = [

    path('', PhotoGallery, name='photo_gallery'),

]