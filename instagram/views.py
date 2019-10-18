from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import datetime as dt
from .models import Profile,Image
from django.contrib.auth.models import User

#Create your views here
#......... this is for login page.........
@login_required(login_url='account/login/')
def index(request):
    all_images = Image.objects.all()
    all_users = Profile.objects.all()
    return render(request,'/home.html',{"all_images":all_images},{"all_user":all_users})

#...............this for explore view function...............
@login_required(login_url='account/login/')
def explore(request):
    return render(request,'/explore.html')

#................this is for profile  view function............
@login_required(login_url='account/login') 
def profile(request):
    return render(request,'/userprofile.html')

#........... for the logout page...................
def logout(request):
     return render(request,'/logout.html')
#....... login page ........................................
def login(request):
    return rended(request,'/login.html')

#.....................uploading page..................
@login_required(login_url='/account/login')
def upload(request):
    current_user = request.user
    p = Profile.objects.filter(id=current_user.id).first()
    imageuploader_profile = Image.objects.filter(imageuploader_profile=p)
    if request.method =='POST':
        form = postForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.imageuploader_profile=p
            post.save
            return redirect('/')
    else:
        form=PostForm
    return render(request,'/upload.html',{"form":form})


    '
