from django.urls import path
from .views import AddImage, Gallery

urlpatterns = [
    path('', Gallery, name='gallery'),
    path('add_image/', AddImage, name='add_image'),

]