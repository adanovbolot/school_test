from django.contrib import admin
from .models import Student, Teacher, ClassChoice, School


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("surname",)}


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass


@admin.register(ClassChoice)
class ClassStudentAdmin(admin.ModelAdmin):
    pass


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
