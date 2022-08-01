from django import forms
from .models import Student, School


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('surname', 'mail', 'date_of_birth', 'class_student', 'address', 'sex', 'photo')


class StudentEmailForm(forms.Form):
    surname = forms.CharField(label='ФИО', widget=forms.TextInput(attrs={'class': 'form-control'}))
    mail = forms.CharField(label='Майл', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Текст', widget=forms.TextInput(attrs={'class': 'form-control'}))


class StudentDeleteForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ('name', 'class_students')
