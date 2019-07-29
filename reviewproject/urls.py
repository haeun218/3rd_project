"""reviewproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
import diaryapp.views
import userapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', diaryapp.views.main, name='main'),
    path('diaryapp/<int:post_id>', diaryapp.views.show, name='show'), 
    path('diaryapp/new', diaryapp.views.new, name='new'),
    path('diaryapp/postcreate', diaryapp.views.postcreate, name='postcreate'),
    path('diaryapp/edit', diaryapp.views.edit, name='edit'),
    path('diaryapp/postupdate/<int:post_id>', diaryapp.views.postupdate, name='postupdate'),
    path('diaryapp/postdelete/<int:post_id>', diaryapp.views.postdelete, name='postdelete'),
    path('userapp/', include('userapp.urls')),
]
