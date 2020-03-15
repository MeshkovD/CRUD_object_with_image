from django.urls import path
from .views import PhotoGallery, picture_page, picture_delete

urlpatterns = [

    path('', PhotoGallery, name='photo_gallery'),
    path('picture_page/<int:id>/', picture_page, name='picture_page'),
    path('picture_delete/<int:id>/', picture_delete, name='picture_delete'),

]