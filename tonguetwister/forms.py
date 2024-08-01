import re

from django import forms
from .models import Articulator, Exercise, Twister, Trivia, Funfact, Profile
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class ArticulatorForm(forms.ModelForm):
    class Meta:
        model = Articulator
        fields = ['text']


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['text']


class TwisterForm(forms.ModelForm):
    class Meta:
        model = Twister
        fields = ['text']


class TriviaForm(forms.ModelForm):
    class Meta:
        model = Trivia
        fields = ['text']


class FunfactForm(forms.ModelForm):
    class Meta:
        model = Funfact
        fields = ['text']


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'id': 'username'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'id': 'email'})
    )
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'id': 'password1'})
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'id': 'password2'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Ktoś już zaklepał taką nazwę :(")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Konto z takim adresem email już istnieje :(")
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if not self.is_password_strong(password1):
            raise ValidationError(
                "Hasełko to więcej niż 8 znaków i składa się z wielkich i małych liter, cyfr i specjalnych znaków :)")
        return password1

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Hasełka do siebie nie pasują :(")

        return cleaned_data

    def is_password_strong(self, password):
        if len(password) < 8:
            return False
        if not re.search(r"[A-Z]", password):
            return False
        if not re.search(r"[a-z]", password):
            return False
        if not re.search(r"[0-9]", password):
            return False
        if not re.search(r"[!@#$%^&*()_+]", password):
            return False
        return True

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            regular_users_group = Group.objects.get(name='Regular Users')
            user.groups.add(regular_users_group)
        return user


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'username', 'placeholder': 'Nazwa użytkownika'})
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password', 'placeholder': 'Hasło'})
    )


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


class AvatarUploadForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']
        widgets = {
            'avatar': forms.FileInput(attrs={
                'class': 'form-control-file',
                'id': 'avatar',
            }),
        }
        labels = {
            'avatar': 'Wybierz awatar'
        }
