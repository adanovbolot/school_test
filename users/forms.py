from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import CustomUser
from django.contrib.auth.models import Group


class CustomUserCreationForm(UserCreationForm):
    # groups = forms.ModelChoiceField(queryset=Group.objects.all())

    class Meta:
        model = CustomUser
        fields = ('username', 'phone_number', 'date_of_birth')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'phone_number', 'date_of_birth', 'groups')


class UserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email')