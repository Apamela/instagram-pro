from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#................class user ...........
class Profile (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio =models.CharField(max_length=60)
    profile_pic = models.ImageField(upload_to='ProfilePicture/')
    
    def __str__(self):
        return self.Profile.user
#..............class Image..................    
class Image (models.Model):
    name = models.CharField(max_length= 30)
    caption = models.CharField(max_length=60)
    image_likes = models.ManyToManyField('profile',default=False,blank=True,related_name='likes')
    profile_pic = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name='comments')
    image_comment = models.ManyToManyField('profile',default=False,blank=True)
    image_image = models.ImageField(upload_to='image')

    def __str__(self):
        return self.name
#........ class Comment................

class comments (models.Model):
    post = models.CharField(max_length=70)
    author = models.ForeignKey('Profile',on_delete=models.CASCADE)

    def __str__(self):
        return self.author



