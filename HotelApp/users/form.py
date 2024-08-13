from django import forms # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore
from .models import Customer 
from crispy_forms.helper import FormHelper # type: ignore
from crispy_forms.layout import Layout, Field # type: ignore
from django.db import models # type: ignore

class UserRegesiterForm(UserCreationForm):
    email = forms.EmailField()
    card_number = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'placeholder': 'Card Number'}))
    card_expiry_date = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'placeholder': 'MM/YY'}))
    card_cvc = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'placeholder': 'CVC'}))
    image = models.ImageField(upload_to='profile_pics', blank=True, null=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'card_number', 'card_expiry_date', 'card_cvc']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']
        
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'      


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model= Customer
        fields = ['image']  
