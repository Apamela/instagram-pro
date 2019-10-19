from django import forms
from .models import Profile,Image
from django.contrib.auth.models import User
 

class PostForm(forms.ModelsForm):
    class Meta:
        model = Image
        fields = ('caption','image')

class SignUpForm(forms.ModelForm):
  class Meta:
    model = Profile
    exclude = ['bio','profile_pic']
