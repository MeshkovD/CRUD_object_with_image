from django import forms

from .models import SimpleAddPicture


class SimpleAddPictureForm(forms.ModelForm):
    class Meta:
        model = SimpleAddPicture
        fields = ('title', 'photo')
