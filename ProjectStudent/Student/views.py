from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse

from Student.models import StudentDB, Course, City


# from Student.models import login


# Create your views here.
def reg(request):
    return render(request, "register.html")


def regdata(request):
    USER = request.POST.get('txtname')
    email = request.POST.get('txtemail')
    PASSWORD = request.POST.get('txtpassword')

    if User.objects.filter(username=USER, email=email, password=PASSWORD).exists():
        return render(request, "register.html", {'data': 'user,password and email already exists'})
    else:
        u1 = User.objects.create_superuser(username=USER, email=email, password=PASSWORD)
        u1.save()
        return redirect('login')


def logdata(request):
    return render(request, "login.html")


def log(request):
    if request.method == 'POST':
        Userid = request.POST.get('txtu')
        pass_word = request.POST.get('txtp')

        user = authenticate(request, username=Userid, password=pass_word)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("invalid user name")
    else:
        return render(request, "login.html")


def home(request):
    return render(request, "home.html")


def add(request):
    City_Name = City.objects.all()
    Course_Name = Course.objects.all()
    return render(request, "add.html", {'Course_data': Course_Name, 'City_data': City_Name})


def main(request):
    name = request.POST.get('txtname')
    age = request.POST.get('txtage')
    phno = request.POST.get('txtphno')
    course = request.POST.get('txtcou')
    city = request.POST.get('txtcity')

    s1 = StudentDB()
    s1.Name = name
    s1.Age = age
    s1.Phno = phno
    s1.Course_Name = Course.objects.get(Course_Name=course)
    s1.City_Name = City.objects.get(City_Name=city)
    s1.save()
    return redirect('add')


def display(request):
    s1 = StudentDB.objects.all()
    return render(request, "display.html", {'data': s1})


def update(request, id):
    City_Name = City.objects.all()
    Course_Name = Course.objects.all()
    m1 = StudentDB.objects.get(id=id)
    if request.method == 'POST':
        m1.Name = request.POST['txtname']
        m1.Age = request.POST['txtage']
        m1.Phno = request.POST['txtphno']
        m1.Course_Name = Course.objects.get(Course_Name=request.POST['txtcou'])
        m1.City_Name = City.objects.get(City_Name=request.POST['txtcity'])
        m1.save()
        return redirect('display')
    return render(request, "update.html", {'data': m1, 'Course_data': Course_Name, 'City_data': City_Name})


def delete(request, id):
    m1 = StudentDB.objects.get(id=id)
    m1.delete()
    return redirect('display')
