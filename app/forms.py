from django.forms import ModelForm
from app.models import Image


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
