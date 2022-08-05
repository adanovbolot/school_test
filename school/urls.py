from django.urls import path
from school import views

urlpatterns = [
    path('school-list/', views.school_list, name='school_list'),
    path('school-detail/<int:pk>/', views.school_detail, name='school_detail'),
    path('student-list/', views.student_list, name='student_list'),
    path('student-detail/<int:pk>/', views.student_detail, name='student_detail'),
    path('add-student/', views.StudentCreateView.as_view(), name='add_student'),
    path('add-school/', views.SchoolCreateView.as_view(), name='add_school'),
    path('send', views.send_message, name='send'),
    path('search/', views.Search.as_view(), name='search'),
    path('class_choice/', views.ClassChoiceFormCreate.as_view(), name='class_sch'),
    path('teacher_create', views.TeacherFormCreate.as_view(), name='teacher_create'),
    path('personal_area/', views.teacher_list, name='teacher'),
    path('student-delete/<int:pk>/', views.student_delete, name='delete'),
    path('student-edit/<int:pk>/', views.student_edit, name='student_edit'),
]
