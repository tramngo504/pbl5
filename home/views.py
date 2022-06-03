from asyncio.windows_events import NULL
from cgitb import html
from datetime import datetime
from logging import exception
from django.shortcuts import redirect, render
from matplotlib import use
# from regex import A
from .models import user as user_model
from .models import pose as pose_model
from django.utils import timezone
from .models import user as InfoUser
from django.shortcuts import get_object_or_404

# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        getuser = user_model.objects.filter(username = username, password = password).first()
        if getuser != None:
            request.session['username'] = username
            request.session['password'] = password
            request.session['password'] = password
            request.session['user_id'] = getuser.user_id
            request.session.set_expiry(300)
            if (getuser.role == 0):
                return redirect("/homeuser/")
            if (getuser.role == 1):
                return redirect("/homeadmin/")
        else:
            return render(request, 'login.html')
    else:
        return render(request,'login.html')

# Admin
def get_home_admin(request, category="pose_id"):
    pose_list = pose_model.objects.filter().order_by(category)
    return render(request, 'adminhome.html', {'pose_list' : pose_list})
def get_pose_add(request):
    return render(request, 'poseAdd.html')
def add_pose(request):
    if request.method == "POST":
        name = request.POST["name"]
        image1 = request.FILES["image1"]
        image2 = request.FILES["image2"]
        image3 = request.FILES["image3"]
        image4 = request.FILES["image4"]
        image5 = request.FILES["image5"]
        image6 = request.FILES["image6"]
        image7 = request.FILES["image7"]
        image8 = request.FILES["image8"]
        image9 = request.FILES["image9"]
        image10 = request.FILES["image10"]

        pose = pose_model.objects.create(name = name,
                                        image1 = image1,
                                        image2 = image2,
                                        image3 = image3,
                                        image4 = image4,
                                        image5 = image5,
                                        image6 = image6,
                                        image7 = image7,
                                        image8 = image8,
                                        image9 = image9,
                                        image10 = image10)
        pose.save()
        return redirect("/homeadmin")
    else:
        return render(request, 'error.html')

def delete_pose(request, id):
    pose = pose_model.objects.get(pose_id=id)
    pose.delete()
    return redirect("/homeadmin/")


def get_pose_edit(request, id):
    pose_list = pose_model.objects.filter()
    pose_id = pose_model.objects.filter(pose_id = id)
    return render(request, 'poseEdit.html', {'pose_list':pose_list, 'pose_id':pose_id})

def edit_pose(request, id):
    if request.method == 'POST':
        pose_id = pose_model.objects.get(pose_id = id)
        pose_id.name = request.POST["name"]
        pose_id.times = pose_id.times
        pose_id.image1 = request.FILES["image1"]
        pose_id.image2 = request.FILES["image2"]
        pose_id.image3 = request.FILES["image3"]
        pose_id.image4 = request.FILES["image4"]
        pose_id.image5 = request.FILES["image5"]
        pose_id.image6 = request.FILES["image6"]
        pose_id.image7 = request.FILES["image7"]
        pose_id.image8 = request.FILES["image8"]
        pose_id.image9 = request.FILES["image9"]
        pose_id.image10 = request.FILES["image10"]
        pose_id.save()
        return redirect('/homeadmin/' )
    else:
        return render(request, 'error.html')
    
def get_pose_find(request):
    if request.method == 'POST':
        find = request.POST["find"]
        if (find != ""):
            pose_list = pose_model.objects.filter(name=find)
            return render(request, 'adminhome.html', {'pose_list' : pose_list})
        else:
            pose_list = pose_model.objects.filter()
            return render(request, 'adminhome.html', {'pose_list' : pose_list})

def get_pose_search(request):
    if request.method == 'POST':
        search = request.POST["search"]
        if (search == "name"):
            pose_list = pose_model.objects.filter().order_by("name")
            return render(request, 'adminhome.html', {'pose_list' : pose_list})
        if (search == "times"):
            pose_list = pose_model.objects.filter().order_by("times")
            return render(request, 'adminhome.html', {'pose_list' : pose_list})

#User

def get_home_user(request):
    print(request.session['user_id'])
    userid = request.session['user_id']
    return render(request, 'userhome.html',{'userid': userid})

def get_register(request):
    return render(request, 'register.html')

def add_register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        user = user_model.objects.create(
                                        username = username,
                                        email = email,
                                        password = password,
                                        )
        user.save()
        return render(request, 'login.html')
    else:
        return render(request, 'register.html')

# def get_home_admin(request, category="pose_id"):
#     pose_list = pose_model.objects.filter().order_by(category)
#     return render(request, 'adminhome.html', {'pose_list' : pose_list})
def detail_view(request, id):
    #userid = request.session['user_id']
    userid = id
    info_user = InfoUser.objects.get(user_id=userid)
    context = {
        'infoUser': info_user,
        'userid' : userid
    }
    print(info_user.password)
    return render(request, 'account.html', context)

def update_user(request, id):
    info_user = get_object_or_404(InfoUser, user_id=id)
    if request.method == 'POST':
        info_user.first_name = request.POST['first_name']
        info_user.last_name = request.POST['last_name']
        info_user.email = request.POST['email']
        info_user.phone = request.POST['phone']
        info_user.address = request.POST['address']
        info_user.date = request.POST['date']
        info_user.save()
    context = {
        'infoUser': info_user,
    }
    return redirect('/homeuser/')


def update_password(request, id):
    info_user = get_object_or_404(InfoUser, user_id=id)
    info_user.password = request.POST['newPassword']
    info_user.save()
    context = {
        'infoUser': info_user,
    }
    return redirect('/homeuser/')

def get_capture_form(request):
    return render(request, 'capture.html')