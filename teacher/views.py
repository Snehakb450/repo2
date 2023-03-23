from django.shortcuts import render

# Create your views here.
def get_teacher_home(request):
    return render(request,"teacher/teacher_home.html")