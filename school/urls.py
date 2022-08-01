from django.urls import path
from school import views

urlpatterns = [
    path('school-list/', views.school_list, name='school_list'),
    path('school-detail/<int:pk>/', views.school_detail, name='school_detail'),
    path('student-list/', views.student_list, name='student_list'),
    path('student-detail/<int:pk>/', views.student_detail, name='student_detail'),
    # path('add-student/', views.StudentCreateView.as_view(), name='add_student'),
    path('add-school/', views.SchoolCreateView.as_view(), name='add_school'),
    path('send', views.send_message, name='send'),
    # path('student-delete/<int:id>', views.student_delete, name='student_delete'),
    # path('<id>/delete', views.delete_view, name='delete_student'),
]
