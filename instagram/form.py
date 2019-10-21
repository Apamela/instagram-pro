from django import forms
from .models import Profile,Image
from django.contrib.auth.models import User
 

class PostForm(forms.ModelsForm):
    class Meta:
        model = Image
        fields = ('caption','image')

class  UserForm(forms.Form):
       your_name= forms.CharField(label='First Name',max_length=30)
       email = forms.EmailField(label = 'Email')