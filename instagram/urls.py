from django.conf.urls import url
from.import views
import datetime as dt
from django.conf import settings
from django.shortcuts import render, redirect

from django.conf.urls.static import static


urlpatterns=[
   url('^$',views.welcome,name='welcome'),
   url('^Profile/$',views.Profile,name = 'profile'),
   url('^$',views.index,name='index'),
   url('upload',views.upload,name ='upload'),         #  url('logout',views.index,{'next_page':'accounts:login'}, name='logout'),
          
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)