from django import forms
from .models import Student, School, ClassChoice, Teacher


class ClassChoiceForm(forms.ModelForm):
    class Meta:
        model = ClassChoice
        fields = ('name', 'teacher', 'student')


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('id', 'surname', 'mail', 'date_of_birth', 'class_student', 'address', 'sex', 'photo')


class StudentEmailForm(forms.Form):
    type = forms.CharField(label='Тема', widget=forms.TextInput(attrs={'class': 'form-control'}))
    mail = forms.CharField(label='Майл', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'form-control'}))


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ('name', 'class_students')


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('class_school', 'item_name')
