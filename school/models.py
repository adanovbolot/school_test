from django.db import models
from .choices_class import SEX_CHOICE, CLASS_SELECTION, CHOICE_OF_SUBJECTS
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


class ClassStudent(models.Model):
    class Meta:
        verbose_name = 'Название класса'
        verbose_name_plural = 'Название классов'

    name_class = models.CharField('Название класса', max_length=100, help_text='например: A, B, Г, Д')
    class_number = models.CharField('Выбор класса', choices=CLASS_SELECTION, max_length=100)

    def __str__(self):
        return f"класс: {self.class_number} имя класса: {self.name_class}"


class Student(models.Model):
    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

    surname = models.CharField('ФИО', max_length=100, help_text='введите ФИО')
    mail = models.EmailField('Email')
    date_of_birth = models.DateField('Дата рождения', help_text='формат: 00.00.0000')
    class_student = models.ForeignKey(ClassStudent, verbose_name='Класс', on_delete=models.RESTRICT)
    address = models.CharField('Адрес', max_length=100)
    sex = models.CharField('Пол', max_length=100, choices=SEX_CHOICE)
    photo = models.ImageField('Фото(необязательно)', upload_to='media/', blank=True, null=True)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return f"Имя ученика: {self.surname}\n Дата рождения: {self.date_of_birth} Класс: {self.class_student}"

    def get_absolute_url(self):
        return f"/school/{self.slug}/"


class Teacher(models.Model):
    class Meta:
        verbose_name = 'учитель'
        verbose_name_plural = 'учителя'

    user = models.OneToOneField(User, on_delete=models.PROTECT)
    phone_number = PhoneNumberField('номер телефона')
    class_student = models.ForeignKey(ClassStudent, on_delete=models.RESTRICT, verbose_name='Класс')
    item_name = models.CharField('Название предмета', choices=CHOICE_OF_SUBJECTS, max_length=100)

    def __str__(self):
        return f"имя учителя: {self.user}классы учителей: {self.class_student}"


class ClassChoice(models.Model):
    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'

    name = models.ForeignKey(ClassStudent, on_delete=models.PROTECT)
    teacher = models.ForeignKey(Teacher, on_delete=models.RESTRICT)
    student = models.ManyToManyField(Student, verbose_name='Ученики')

    def __str__(self):
        return f"название класса: {self.name} учитель: {self.teacher}"


class School(models.Model):
    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = 'Школы'

    name = models.CharField('Название школы', max_length=100, unique=True)
    class_students = models.ForeignKey(ClassChoice, verbose_name='класс', on_delete=models.RESTRICT, related_name='school_class')
    draft = models.BooleanField(default=False, verbose_name='Черновик')
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return f"название школы: {self.name}"

    def get_absolute_url(self):
        return f"/school/{self.slug}/"


