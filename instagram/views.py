from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import datetime as dt
from .models import Profile,Image,Comment
from django.contrib.auth.models import User
from .form import ProfileForm,ImageForm,CommentForm

#Create your views here 
    
@login_required(login_url='/accounts/login/') 
def welcome(request):
    all_image = Image.objects.all()
    current_user = request.user
    # all_user= Profile.get_all_instagram()
    # profir = Profile.objects.filter(id = current_user.id).first()
    return render(request,'welcome.html', {"all_image": all_image})
@login_required(login_url='/accounts/login/')
def your_profile(request):
    current_user = request.user
    profile = Profile.objects.filter(id = current_user.id).first()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            caption = form.save(commit=False)
            caption.user = current_user
            caption.save()
            return redirect('profile')

    else:
        form = ProfileForm()
    return render(request, 'profile2.html', {"form": form})

   
@login_required(login_url='/accounts/login/')
def add_Comment(request, image_id):
    current_user = request.user
    image_item = Image.objects.filter(id = image_id).first()
    profiless = Profile.objects.filter( user = current_user.id).first()
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.posted_by = profiless
            comment.commented_image = image_item
            comment.save()
            return redirect('welcome')

    else:
        form = CommentForm()
    return render(request, 'comment.html', {"form": form, "image_id": image_id})




@login_required(login_url='/accounts/login/')
def profile(request):

    current_user = request.user
    prof_images = Image.objects.filter(user = current_user)
    profile = Profile.objects.filter(user = current_user).first()
    return render(request, 'profile.html', {"prof_images":prof_images, "profile":profile})



@login_required(login_url='/accounts/login/')
def upload(request):

    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('welcome')

    else:
        form = ImageForm()
    return render(request, 'upload.html', {"form": form})



def like(request,id):
    
    likes=1
    image = Image.objects.get(id=id)
    image.like = image.like+1
    image.save()    
    return redirect("/")