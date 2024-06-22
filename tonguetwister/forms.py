from django import forms
from .models import Articulator, Exercise, Twister, Trivia, Funfact
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


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
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

