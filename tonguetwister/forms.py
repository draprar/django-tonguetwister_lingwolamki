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
            raise ValidationError("Username is already taken")
        return username

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
