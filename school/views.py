from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.core.mail import send_mail
from .models import Student, School, Teacher
from .forms import StudentForm, SchoolForm, StudentEmailForm, ClassChoiceForm, TeacherForm
from django.views.generic import CreateView, ListView


def teacher_list(request):
    teacher_list = Teacher.objects.all()
    return render(request, 'school/personal_area.html', {'teacher_list': teacher_list})


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


class StudentCreateView(CreateView):
    template_name = 'school/create_student.html'
    queryset = Student.objects.all()
    form_class = StudentForm
    success_url = reverse_lazy('send')


def send_message(request):
    if request.method == "POST":
        form = StudentEmailForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['surname'], form.cleaned_data['content'], form.cleaned_data['mail'],
                             ['adanovbolot312@gmail.com'], fail_silently=False)
            if mail:
                messages.success(request, 'Письмо отправлено!')
                return redirect('create_student')
            else:
                messages.error(request, 'Ошибка отправки!')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = StudentEmailForm()
    return render(request, 'school/send_message.html', {'form': form})


class SchoolCreateView(CreateView):
    template_name = 'school/create_school.html'
    form_class = SchoolForm
    success_url = reverse_lazy('school_list')


class ClassChoiceFormCreate(CreateView):
    template_name = 'school/create_class.html'
    form_class = ClassChoiceForm
    success_url = reverse_lazy('school_list')


class TeacherFormCreate(CreateView):
    template_name = 'school/create_teacher.html'
    form_class = TeacherForm
    success_url = reverse_lazy('school_list')


class Search(ListView):
    template_name = 'school/student_list.html'
    context_object_name = 'sch_list'
    paginate_by = 5

    def get_queryset(self):
        return Student.objects.filter(surname__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context
