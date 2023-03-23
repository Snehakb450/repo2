from django.urls import path
from . import views
app_name='teacher'

urlpatterns = [
    path('teacher_home/',views.get_teacher_home, name="teacher_home")
]
