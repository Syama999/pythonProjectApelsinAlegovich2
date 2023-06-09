from django import forms
from .models import Categories, RealEstate
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    subject = forms.CharField(label = 'Тема', widget = forms.TextInput(attrs = {'class' :'form-control',}))
    content = forms.CharField(label = 'Текст', widget = forms.Textarea(attrs = {'class' :'form-control',"rows": 5}))
    captcha = CaptchaField()

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label = 'Имя пользователя', widget = forms.TextInput(attrs = {'class' :'form-control','autocomplete':"off"}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class RealestateForm(forms.ModelForm):
    class Meta:
        model = RealEstate
        fields = ['description', 'photo', 'adress', 'category']
        widgets = {
            'description':forms.TextInput(attrs = {'class':'form-control'}),
            'adress': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),

        }
    def _clean_description(self):
        description = self.cleaned_data['description']
        if re.match(r'\d', description):
            raise ValidationError('Название не должно начинается с цифры')
        return description