from django.shortcuts import render

# Create your views here.
def get_student_home(request):
    return render(request,"student/student_home.html")

def get_student_login(request):
    return render(request,"student/student_login.html")

def get_student_masterpage(request):
    return render(request,"student/student_masterpage.html")

def get_student_profile(request):
    return render(request, "student/student_profile.html")

def get_student_password(request):
    return render(request, "student/student_password.html")

def get_student_details(request):
    return render(request,"student/student_details.html")