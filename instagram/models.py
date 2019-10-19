from django.db import models
from django.contrib.auth.models import User
#  Create your models here.




# ........class user..............................................................................................................
# class user(models.Model):
#     email = models.CharField(max_length=60)
#     username = models.CharField(max_length=60)
#     password =models .CharField(max_length = 60)
#     def __str__(self):
#         return  self.email 

# ........................................class profile..................................................................................................

class Profile (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio =models.CharField(max_length=60)
    profile_pic = models.ImageField(upload_to='ProfilePicture/')
    
    def __str__(self):
        return self.first_name
 
# ..............class Image..........................................................................................................................   
class Image (models.Model):
    name = models.CharField(max_length= 30)
    caption = models.CharField(max_length=60)
    image_likes = models.ManyToManyField('profile',default=False,blank=True,related_name='likes')
    profile_pic = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name='comments')
    image_comment = models.ManyToManyField('profile',default=False,blank=True)
    image_image = models.ImageField(upload_to='image')
     
    def save_Image(self):
        self.save()
    def delete_Image(self):
        self.delete()
    def update_caption(self):
        self.update()
    def __str__(self):
        return self.name
