from django.db import models


class Twister(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class Articulator(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text
