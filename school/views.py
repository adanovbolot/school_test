from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Student, ClassChoice, School
from django.core.mail import BadHeaderError, send_mail


def school_list(request):
    sch_list = School.objects.all()
    return render(request, 'school/school_list.html', {'sch_list': sch_list})


def school_detail(request, pk):
    sch_detail = get_object_or_404(School, pk=pk)
    return render(request, 'school/school_detail.html', {'sch_detail': sch_detail})


def student_list(request):
    s_list = Student.objects.all()
    return render(request, 'school/student_list.html', {'s_list': s_list})


def student_detail(request, pk):
    student_detail = get_object_or_404(Student, pk=pk)
    return render(request, 'school/student_detail.html', {'student_detail': student_detail})


# def data_detail(request, pk):
#     data_detail = get_object_or_404(Student, pk=pk)
#     return HttpResponse(request, 'school/student_detail.html', {'data_detail': data_detail})
