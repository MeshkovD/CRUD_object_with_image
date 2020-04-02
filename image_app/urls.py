from django.urls import path
from .views import PhotoGallery, PicturePage, PictureDelete, picture_edit

urlpatterns = [

    path('', PhotoGallery, name='photo_gallery'),
    path('picture_page/<int:id>/', PicturePage.as_view(), name='picture_page'),
    path('picture_delete/<int:id>/', PictureDelete.as_view(), name='picture_delete'),
    path('picture_edit/<int:id>/', picture_edit, name='picture_edit'),

]
