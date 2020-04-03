from django.urls import path
from .views import PhotoGallery, PicturePage, PictureDelete, PictureCreate, PictureUpdate

urlpatterns = [

    path('', PhotoGallery.as_view(), name='photo_gallery'),
    path('picture_page/<int:id>/', PicturePage.as_view(), name='picture_page'),
    path('picture_delete/<int:id>/', PictureDelete.as_view(), name='picture_delete'),
    path('picture_create/', PictureCreate.as_view(), name='picture_create'),
    path('picture_update/<int:id>/', PictureUpdate.as_view(), name='picture_update'),

]
