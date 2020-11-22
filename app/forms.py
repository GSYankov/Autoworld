from django import forms
from app.models import Image

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
