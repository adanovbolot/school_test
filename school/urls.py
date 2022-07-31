from django.urls import path
from school import views

urlpatterns = [
    path('school-list/', views.school_list, name='school_list'),
    path('school-detail/<int:pk>/', views.school_detail, name='school_detail'),
    path('student-list/', views.student_list, name='student_list'),
    path('student-detail/<int:pk>/', views.student_detail, name='student_detail'),
]
