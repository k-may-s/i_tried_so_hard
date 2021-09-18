from django.db import models


class Client(models.Model):
    last_name = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=60)
    address = models.CharField(max_length=120, blank=True)
    rate = models.CharField(max_length=60)

# TODO: Не переиспользуются id клиента
