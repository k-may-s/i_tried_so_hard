from django.contrib.auth.base_user import BaseUserManager
from django.db import models


class User(models.Model):
    login = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    email = models.EmailField(unique=True, max_length=60)
    date_created = models.DateTimeField(auto_now_add=True)
    last_login_date = models.DateTimeField(auto_now=True, blank=True)
    active = models.BooleanField(default=True)

    objects = BaseUserManager()

    def __str__(self):
        return self.email
