from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta


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
    login_streak = models.PositiveIntegerField(default=1)
    last_login_date = models.DateField(auto_now=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def update_login_streak(self):
        today = timezone.now().date()

        if self.last_login_date == today:
            return

        if self.last_login_date == today - timedelta(days=1):
            self.login_streak += 1
        else:
            self.login_streak = 1

        self.last_login_date = today
        self.save()

    def __str__(self):
        return f'{self.user.username} Profile'


class UserProfileArticulator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    articulator = models.ForeignKey(Articulator, on_delete=models.CASCADE)


class UserProfileExercise(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)


class UserProfileTwister(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    twister = models.ForeignKey(Twister, on_delete=models.CASCADE)
