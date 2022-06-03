from django.contrib import admin
from matplotlib.style import use
from home.models import user, pose
from .models import poseUser, ListPoseUser, InfoUser

# Register your models here.
admin.site.register(user)
admin.site.register(pose)
admin.site.register(ListPoseUser)
