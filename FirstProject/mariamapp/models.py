from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Applicant(models.Model):
    name = models.CharField('Applicant name',max_length=300)
    address = models.CharField(max_length=400)
    zip_code = models.CharField('Zip Code',max_length=300)
    des = models.TextField('About yourslf', blank=True)
    phone = models.IntegerField('Contact Phone')
    web = models.URLField('Web Address', blank=True)
    Male='Male'
    Female='Female'
    GENDER_CHOICES=(('M', 'Male'), ('F', 'Female'))
    gender = models.CharField(max_length=6, choices= GENDER_CHOICES, default="")
    email_address = models.EmailField('Email Address', blank=True)

    def __str__(self):
        return self.name
