from django.conf.urls import url
from.import views
from django.conf import settings
from django.shortcuts import render, redirect
from django.conf.urls.static import static


urlpatterns=[
   url('^$',views.welcome,name='welcome'),
   url(r'^profile$',views.profile, name='profile'),
   url(r'^upload$',views.upload,name='upload'),
   url(r'^yourprofile',views.your_profile,name='change')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)