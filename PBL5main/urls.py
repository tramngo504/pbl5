"""PBL5main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home import views as home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.login_view),
    path('homeadmin/', home.get_home_admin),
    path('homeuser/', home.get_home_user),
    path('addPoseForm/', home.get_pose_add),
    path('addPose/', home.add_pose),
    path('delete/<int:id>/', home.delete_pose),
    path('editPoseForm/<int:id>/', home.get_pose_edit),
    path('editPose/<int:id>/', home.edit_pose),
    path('findPose/', home.get_pose_find),
    path('searchPose/', home.get_pose_search),
    path('registerForm/', home.get_register),
    path('register/', home.add_register),
    path('accountview/<int:id>/', home.detail_view),
    path('update/<int:id>/', home.update_user),
    path('updatepassword/<int:id>/', home.update_password),
    path('capture/', home.get_capture_form),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)