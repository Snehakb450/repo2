from django.urls import path
from . import views
app_name='student'

urlpatterns = [
    path ('student_home/',views.get_student_home, name="student_home"),
    path('student_login/',views.get_student_login, name="student_login"),
    path('student_masterpage/',views.get_student_masterpage, name="student_masterpage"),
    path('student_profile/',views.get_student_profile, name="student_profile"),
    path('student_password/',views.get_student_password, name="student_password")
]
