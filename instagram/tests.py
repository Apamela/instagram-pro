from django.test import TestCase
from .models import Profile,Image,Comment
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestClass(TestCase):
    
    # Setup method
    def setUp(self):
        self.user = User.objects.create(id = 1,username = 'pop')
        self.profile = Profile(firstname = 'hon',lastname = 'pol',profile_photo = 'top.jpeg', bio = 'singer', user = self.user)
 
    # Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    # testing the save method
    def test_save_method(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) >= 1)
        
    def test_delete_method(self):
       self.profile.save_profile()

   
class CommentTestClass(TestCase):
     # Setup method
    def setUp(self):
        self.comment = Comments.objects.create(comment ="all the best")
        
    # Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comments))

    # testing the save method
    def test_save_method(self):
        self.comment.save_comments()
        comment = Comments.objects.all()
        self.assertTrue(len(comment) > 0)
        
    def test_delete_method(self):
        self.comment.save_comments()
        self.comment.delete_comments()
        comment = Comments.objects.all()
        self.assertTrue(len(comment) >= 0)

class ImageTestClass(TestCase):
    
    
        
    def tearDown(self):
        Image.objects.all().delete()
        Profile.objects.all().delete()

    # Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))
        
    # testing the save method
    def test_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) >= 1)
        
    def test_delete_method(self):
        self.image.save_image()
        images = self.image.delete_image()
        deleted = Image.objects.all()
        self.assertTrue(len(deleted) <= 0)
