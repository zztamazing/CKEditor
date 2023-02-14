"""testCKEditor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include, re_path
from django.views.static import serve

import passages
from .settings import MEDIA_ROOT

"""
username: admin
password: admin
"""
urlpatterns = [

    path('admin/', admin.site.urls),
    path('passage/', include('passages.urls')),

    # 上传media的文件可以被查看，这个很重要，更后边的一个bug有关
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    # ckckeditor图片上传
    path('ckeditor/', include('ckeditor_uploader.urls')),


]
