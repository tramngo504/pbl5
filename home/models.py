from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

class user(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=40,null=False)
    password = models.CharField(max_length=40,null=False)
    first_name = models.CharField(max_length=40, default=None, null=True)
    last_name = models.CharField(max_length=40, default=None, null=True)
    email = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=10, default=None, null=True)
    address = models.CharField(max_length=500, default=None, null=True)
    date = models.DateTimeField(default=timezone.now, null=True)
    gender = models.BooleanField(default=True, null=True)
    role = models.BooleanField(default=False, null=True)

def __str__(self):
    return f"{self.user_id}, {self.username}, {self.password}, {self.first_name}, {self.last_name},{self.email}, {self.phone},{self.address}, {self.date},{self.gender}, {self.role}"

class pose(models.Model):
    pose_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    times = models.IntegerField(null=True)
    image1 = models.ImageField(upload_to="images", null=False, default=None)
    image2 = models.ImageField(upload_to="images", null=False, default=None)
    image3 = models.ImageField(upload_to="images", null=False, default=None)
    image4 = models.ImageField(upload_to="images", null=False, default=None)
    image5 = models.ImageField(upload_to="images", null=False, default=None)
    image6 = models.ImageField(upload_to="images", null=False, default=None)
    image7 = models.ImageField(upload_to="images", null=False, default=None)
    image8 = models.ImageField(upload_to="images", null=False, default=None)
    image9 = models.ImageField(upload_to="images", null=False, default=None)
    image10 = models.ImageField(upload_to="images", null=False, default=None)

def __str__(self):
    return f"{self.pose_id}, {self.name}, {self.times}, {self.image1}, {self.image2},{self.image3}, {self.image4},{self.image5}, {self.image6},{self.image7}, {self.image8},{self.image9}, {self.image10}"



class poseUser(models.Model):
    idPose = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    times = models.IntegerField(null=False, default=0)
    image1 = models.ImageField(upload_to="images", null=False, default=None)
    image2 = models.ImageField(upload_to="images", null=False, default=None)
    image3 = models.ImageField(upload_to="images", null=False, default=None)
    image4 = models.ImageField(upload_to="images", null=False, default=None)
    image5 = models.ImageField(upload_to="images", null=False, default=None)
    image6 = models.ImageField(upload_to="images", null=False, default=None)
    image7 = models.ImageField(upload_to="images", null=False, default=None)
    image8 = models.ImageField(upload_to="images", null=False, default=None)
    image9 = models.ImageField(upload_to="images", null=False, default=None)
    image10 = models.ImageField(upload_to="images", null=False, default=None)
    advantage = models.TextField(null=False)
    excepts = models.TextField(null=False)
    exercise = models.TextField(null=False)

class InfoUser(AbstractUser):
    phone = models.CharField(max_length=10, default="0123456789")
    address = models.CharField(max_length=500, default="Viet Nam")
    date = models.DateTimeField(default=timezone.now)
    gender = models.BooleanField(default=True)

class ListPoseUser(models.Model):
    idPose = models.ForeignKey(poseUser, primary_key=True, on_delete=models.CASCADE)
    user_id = models.ForeignKey(InfoUser, on_delete=models.CASCADE)
    score = models.IntegerField()

    class Meta:
        unique_together = (('idPose', 'user_id'),)




