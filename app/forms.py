from django import forms
from app.models import Image, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from core.BootstrapFormMixin import BootstrapFormMixin



class RegisterForm(UserCreationForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_form()

    class Meta:
        model = User
        fields = ('username', 'email')
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email', False)
        if not email:
            raise forms.ValidationError('Email is required')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username', False)
        if not username:
            raise forms.ValidationError('username is required')
        return username


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_picture',)
