from django.conf.urls import url
from.import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
             
             url('',views.index,name='index'),
             url('profile',views.profile,name = 'profile'),
             url('login',views.login,name='login'),
             url('logout',views.index,{'next_page':'accounts:login'}, name='logout'),
          
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)