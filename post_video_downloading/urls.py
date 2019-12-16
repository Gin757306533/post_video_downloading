"""post_video_downloading URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from post_video_downloading.views import index, upload_picture, acc_login, test, \
    detect_finished_and_celebrity_incide, pawan_video_display, lialan
from django.conf.urls.static import static
from django.conf import settings
import django
urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload_picture/', upload_picture),
    path('login/', acc_login),
    path('index/', index),
    path('test/', test),
    path('detect_finished_and_celebrity_incide/', detect_finished_and_celebrity_incide),
    path('pawan_video_display/', pawan_video_display),
    path('lialan/', lialan),
    # re_path(r'^media/photos/(?P<path>.*)', django.views.static.serve, {'document_root': 'media/photos'}),
    re_path('^$', index),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
