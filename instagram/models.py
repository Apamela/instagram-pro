from django.db import models 
from tinymce.models import HTMLField
from django.contrib.auth.models import User
#  Create your models here.

# ........................................class profile..................................................................................................

class Profile (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.CharField(max_length=60)
    profile_pic = models.ImageField(upload_to='ProfilePicture/')
    date = models.DateTimeField(auto_now_add=True, null= True)
    def __str__(self):
        return self.user
    def save_profile(self):
        self.save()
    # def get_all_instagram(cls):
    #     instagram= cls.objects.all()
    #     return instagram
    def delete_profile(self):
        self.delete()
    @classmethod
    def update_profile(cls,id,value):
        cls.objects.filter(id = id).update(user_id = new_user)

    
# ..............class Image..........................................................................................................................   
class Image (models.Model):
    name = models.CharField(max_length= 30)
    image_caption = models.CharField(max_length=60)
    image_likes = models.ManyToManyField('profile',default=False,blank=True,related_name='likes')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image_comment = models.ManyToManyField('profile',default=False,blank=True,related_name='comment')
    image_image = models.ImageField(upload_to='image')
    date = models.DateTimeField(auto_now_add=True, null= True) 
    def save_Image(self):
        self.save()

    def delete_Image(self):
        self.delete()

    def update_caption(self):
        self.update()
    
    @classmethod
    def get_all_image(cls):
        images = cls.objects.all()
        return images