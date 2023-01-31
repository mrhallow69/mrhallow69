from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from LibraryD.models import Student, Books, Course


# Create your views here.

def home(request):
    return render(request, 'home.html')


def stulog(request):
    return render(request, "login.html")


def stulogdata(request):
    if request.method == 'POST':
        User_id = request.POST.get('txtu')
        Password = request.POST.get('txtp')

        user = authenticate(username=User_id, password=Password)
        if user is not None:
            login(request, user)
            return redirect('studenthome')
        else:
            return HttpResponse('invalid details')
    return render(request, 'login.html')


def adminlog(request):
    return render(request, "adminlogin.html")


def adminlogdata(request):
    if request.method == 'POST':
        user_id = request.POST.get('txtuid')
        Pass_word = request.POST.get('txtpwd')
        user1 = authenticate(username=user_id, password=Pass_word)
        if user1 is not None and not user1.is_superuser:
            login(request, user1)
            return redirect('adminhom')
        else:
            return HttpResponse('invalid Details')
    return render(request, "adminlogin.html")


def adminreg(request):
    return render(request, 'adminreg.html')


def adregdata(request):
    if request.method == "POST":
        u_name = request.POST.get('mj')
        u_email = request.POST.get('text1')
        u_pass = request.POST.get('htpasswd')
        if User.objects.filter(Q(username=u_name) | Q(email=u_email) | Q(password=u_pass)).exists():
            return render(request, 'adminreg.html', {'data': "user name is alraedy exit"})
        else:
            u1 = User.objects.create_user(username=u_name, email=u_email, password=u_pass)
            u1.save()
            return render(request, 'adminlogin.html')

    return render(request, 'adminreg.html')


def studreg(request):
    return render(request, "studreg.html")


def studregdata(request):
    User_name = request.POST.get('dj1')
    Email = request.POST.get('dj2')
    Password = request.POST.get('dj3')

    if User.objects.filter(username=User_name, email=Email, password=Password).exists():
        return render(request, 'studreg.html', {'data': 'credentials already exists'})
    else:
        s1 = User.objects.create_superuser(username=User_name, email=Email, password=Password)
        s1.save()
        return redirect('stulog')


def adminhome(request):
    return render(request, 'adminhome.html')


def studenthome(request):
    return render(request, "studenthome.html")


def add(request):
    Stud_Name = Student.objects.all()
    Book_Name = Books.objects.all()
    Course_Name = Course.objects.all()
    return render(request, "readtable.html",
                  {'Student_data': Stud_Name, 'Book_data': Book_Name, 'Course_data': Course_Name})


def main(request):
    Course_Name = Course.objects.all()
    s1 = Student()
    s1.Stud_Name = request.POST['txtnm']
    s1.Stud_Phno = request.POST['txtnu']
    s1.Stud_Sems = request.POST['txtsem']
    s1.Stud_Password = request.POST['txtpsw']
    s1.Course_Name = Course.objects.get(Course_Name=request.POST['txtcou'])
    s1.save()

    return render(request, "readtable.html")


def display(request):
    s2 = Student.objects.all()
    return render(request, "display.html", {'data': s2})


def addbook(request):
    Course_Name = Course.objects.all()
    if request.method == 'POST':
        Course_Name = request.POST.get('cour')
        Book_Name = request.POST.get('txtbook')
        Author_Name = request.POST.get('Author')
    return render(request, "addbook.html", {'Course_data': Course_Name})


def issuebook(request):
    Book_Name = Books.objects.all()
    if request.method == 'POST':
        Stu_name = request.POST.get('name')
        Book_Name = request.POST.get('book')
        start_date = request.POST.get('sdate')
        end_date = request.POST.get('edate')
        return redirect('issueb')
    return render(request, 'Issuebook.html',
                  {'Book_data': Book_Name})


def displaybook(request):
    B2 = Books.objects.all()
    return render(request, "displaybook.html", {'data1': B2})
