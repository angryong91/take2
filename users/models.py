from django.db import models

class user(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)