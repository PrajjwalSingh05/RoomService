from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth  import authenticate,login,logout
from .models import *
# from room import  *
def index(request):
    return render(request, 'index.html')
# Create your views here.
def login(request):
    error=""
    if request.method=='POST':
        u=request.POST['uname']
        p=request.POST['pswd']
        user=auth.authenticate(username=u,password=p)
        try:
            if user.is_staff:
                auth.login(request,user)
                error="no"
            elif user is not None:
                auth.login(request,user)
                error="not"
            else:
                error="yes"
        except:
            error="yes"
    d={'error':error}
    return render(request, 'login.html',d)

# cahnges
def contact(request):
    return render(request,'Contact us.html')
def admin_home(request):
    return render(request,'admin_home.html')
def signup(request):
    error = ""
    if request.method == 'POST':
        f=request.POST['fname']
        l=request.POST['lname']
        e=request.POST['email']
        c=request.POST['contact']
        dob=request.POST['dob']
        pd=request.POST['pwd']
        g=request.POST['gender']
        i=request.FILES['profile_pic']
        try:
            user=User.objects.create_user(first_name=f,last_name=l,username=e,password=pd)
            Signup.objects.create(user=user,moblie=c,image=i,gender=g,dob=dob)
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'signup.html',d)
def user_home(request):
    return render(request,'user_home.html')
# def user_navigation(request):
#     return render(request,'user_navigation.html');
def logout(request):
    auth.logout(request)
    return redirect('/')
def add_room(request):
    error = ""
    if request.method == 'POST':
        rnum=request.POST['roomno']
        # l = request.POST['lname']
        rtype=request.POST['rtype']
        rprice=request.POST['price']
        rstatus=request.POST['status']
        rimage=request.FILES['image']
        try:
            Room.objects.create(room_no=rnum,price=rprice,type=rtype,image=rimage,status=rstatus)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}

    return render(request,'add_room.html',d)
def view_room_admin(request):
    data=Room.objects.all()
    d={'data':data}
    return render(request,'view_room_admin.html',d)
def delete_room(request,id):
    data=Room.objects.get(id=id)
    data.delete()
    return redirect('view_room_admin')
def delete_booking(request,id):
    data = Booking.objects.get(id=id)
    data.delete()
    return redirect('my_booking')
def edit_room(request,id):
    error=""
    data=Room.objects.get(id=id)
    if request.method=='POST':
        rnum = request.POST['roomno']
        # l = request.POST['lname']
        rtype = request.POST['rtype']
        rprice = request.POST['price']
        rstatus = request.POST['status']
        data.room_no=rnum
        data.price=rprice
        data.type=rtype
        data.status=rstatus
        try:
            i=request.FILES['room_img']
            data.image=i
        except:
            pass

        try:
            data.save()
            error="no"
        except:
            error="yes"
    d={'data':data,'error':error}
    return render(request,'edit_room.html',d)

def view_user(request):
    data=Signup.objects.all()
    d={'data':data}
    return render(request,'view_user.html',d)
def delete_user(request,id):
    data=User.objects.get(id=id)
    data.delete()
    return redirect('view_user')
def view_room_user(request):
    data=Room.objects.all()
    d={'data':data}
    return render(request,'view_room_user.html',d)
def book_room(request,id):
    user=request.user
    data=Room.objects.get(id=id)
    data2=Signup.objects.get(user=user)
    error=""
    if request.method=='POST':
        f=request.POST['fname']
        l=request.POST['lname']
        f=f+" "+l
        e=request.POST['email']
        c1=request.POST['contact']
        c2=request.POST['contact2']
        bd=request.POST['booking_date']
        sd=request.POST['select_days']
        g=request.POST['gender']
        p=request.POST['price']
        dob1=request.POST['dob']
        r=request.POST['roomno']
        p=int(p)*int(sd)
        try:
            Booking.objects.create(room_no=r,full_name=f,email_id=e,contact1=c1,gender=g,contact2=c2,booking_date=bd,
                                   total_days=sd,price=p,dob=dob1,status="pending")
            error="no"
        except:
            error="yes"

    d={'data2':data2,'data':data,'error':error}
    return render(request,'book_room.html',d)
def my_booking(request):
    data=Booking.objects.all()
    d={'data':data}
    return render(request,'my_booking.html',d)



def view_booking_admin(request):
    data = Booking.objects.all()
    d = {'data':data}
    return render(request,'view_booking_admin.html',d)

def change_status(request,id):
    error=""
    data = Booking.objects.get(id=id)
    if request.method=='POST':
        s = request.POST['rstatus']
        data.status=s
        try:
            data.save()
            error="no"
        except:
            error="yes"
    d = {'data':data,'error':error}
    return render(request,'change_status.html',d)

def change_password_admin(request):
    error=""
    if request.method=='POST':
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'change_password_admin.html',d)


def change_password_user(request):
    error=""
    if request.method=='POST':
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'change_password_user.html',d)


def edit_profile(request):
    error=""
    user=request.user
    data=User.objects.get(id=request.user.id)
    data2=Signup.objects.get(user=user)
    if request.method=='POST':
        error=""
        f=request.POST['fname']
        l=request.POST['lname']
        c=request.POST['contact']
        g=request.POST['gender']
        dob=request.POST['dob']
        data.first_name=f
        data.last_name=l
        data2.mobile=c
        data2.gender=g
        data2.dob=dob
        try:
            i=request.FILES['image']
            data2.image=i
            data2.save ()
            error="no"
        except:
            error="yes"
        try:
            data.save()
            data2.save()
            error="no"
        except:
            error="yes"

    d={'data2':data2,'error':error}
    return render(request,'edit_profile.html',d)

def feedback(request):
    error=""
    user=request.user
    data=Signup.objects.get(user=user)
    if request.method=='POST':
        n=request.POST['fname']
        c=request.POST['fphone']
        e=request.POST['femail']
        f=request.POST['fcomment']
        try:
            Feedback.objects.create(name=n,email=e,contact=c,feedback=f)
            error="no"
        except:
            error="yes"
    d={'data':data,'error':error}
    return render(request,'feedback.html',d)

def view_feedback(request):
    data=Feedback.objects.all()
    d={'data':data}
    return render(request,'view_feedback.html',d)

def delete_feedback(request,id):
    data=Feedback.objects.get(id=id)
    data.delete()
    return redirect('view_feedback')
