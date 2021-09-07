from django.db import models


class AuthUser(models.Model):
    login = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
