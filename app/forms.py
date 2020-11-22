from django import forms
from app.models import Image
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
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

    def clean_password2(self):
        return

    def _post_clean(self):
        super()._post_clean()
        return


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
