from django.db import models
from datetime import datetime


# Create your models here.


class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField(blank=True)
    tuber_id = models.IntegerField()
    user_id = models.IntegerField(blank=True)
    created_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email
