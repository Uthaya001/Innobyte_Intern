from django.db import models


class login(models.Model):
    username=models.CharField(max_length=16)
    password=models.CharField(max_length=8)