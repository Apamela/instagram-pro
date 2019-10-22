from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import datetime as dt
from .models import Profile,Image
from django.contrib.auth.models import User
from .form import ProfileForm,ImageForm

#Create your views here 
    
 
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

   
# @login_required(login_url='/accounts/login/')
# def photo(request,photo_id):
#     try:
#         photo = photo.objects.get(id = photo_id)
#     except DoesNotExist:
#         raise Http404()
#     return render(request,"welcome.html", {"photo":photo})

@login_required(login_url='/accounts/login/')
def profile(request):

    current_user = request.user
    prof_images = Image.objects.filter(user = current_user)
    profile = Profile.objects.filter(user = current_user).first()
    return render(request, 'profile.html', {"prof_images":prof_images, "profile":profile})



# @login_required(login_url='/accounts/login/')
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



def following(request):
    followingss = Followers.objects.filter(user_from = request.user)

def likes(request,id):
    
    likes=1
    image = Image.objects.get(id=id)
    image.likes = image.likes+1
    image.save()    
    return redirect("/")