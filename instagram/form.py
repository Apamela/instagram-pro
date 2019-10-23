from django import forms
from .models import Profile,Image,Comment
from django.contrib.auth.models import User
 

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','firstname','lastname','Bio']

class  ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['date','image_likes','image_comment','user']
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = [ 'posted_by','photo']