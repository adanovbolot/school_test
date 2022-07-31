from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Student, ClassStudent, ClassChoice, School
from django.core.mail import BadHeaderError, send_mail


def school_list(request):
    posts = School.objects.all()
    return render(request, 'school/school_list.html', {'posts': posts})


def school_detail(request, pk):
    post = get_object_or_404(School, pk=pk)
    return render(request, 'school/school_detail.html', {'post': post})


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'school/student_detail.html', {'student': student})
