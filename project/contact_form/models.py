from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    message = models.TextField(max_length=1000)
