# app_name/models.py

from django.db import models

class Vote(models.Model):
    value = models.CharField(max_length=10)

    def __str__(self):
        return self.value
