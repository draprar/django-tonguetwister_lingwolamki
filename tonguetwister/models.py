from django.db import models
from django.contrib.auth.models import User


class Twister(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class Articulator(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class Exercise(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class Trivia(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class Funfact(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    login_streak = models.PositiveIntegerField(default=0)
    last_login_date = models.DateField(auto_now=True)

    def update_login_streak(self):
        from django.utils import timezone
        if self.last_login_date < timezone.now().date():
            self.login_streak += 1
            self.last_login_date = timezone.now().date()
            self.save()

    def __str__(self):
        return f'{self.user.username} Profile'
