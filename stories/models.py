from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Post(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    date = models.DateField(default=datetime.now)
    avatar = models.CharField(max_length=500)
    body = models.TextField()

    def __str__(self):
        return str(self.date) + ' | ' + str(self.author) + ' | ' + self.title
