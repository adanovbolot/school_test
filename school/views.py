from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DeleteView, FormView
from .models import Student, School
from .forms import StudentForm, SchoolForm, StudentEmailForm
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


# class StudentCreateView(CreateView):
#     template_name = 'school/create_student.html'
#     form_class = StudentForm
#     success_url = reverse_lazy('school_list')


def send_message(request):
    if request.method ==  "POST":
        form = StudentEmailForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['surname'], form.cleaned_data['content'], form.cleaned_data['mail'], ['adanovbolot312@gmail.com'], fail_silently=False)
            if mail:
                messages.success(request, 'Письмо отправлено!')
                return redirect('school_list')
            else:
                messages.error(request, 'Ошибка отправки!')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = StudentEmailForm()
    return render(request, 'school/create_student.html', {'form': form})

# class StudentFormView(FormView):
#     template_name = 'school/create_student.html'
#     form_class = StudentForm
#     success_url = '/thanks/'
#     print('ok')


class SchoolCreateView(CreateView):
    template_name = 'school/create_school.html'
    form_class = SchoolForm
    success_url = reverse_lazy('school_list')
