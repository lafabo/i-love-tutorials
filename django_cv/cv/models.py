from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    mail = models.EmailField()
    phone = models.CharField(max_length=10)
    skype = models.CharField(max_length=30)
    website = models.URLField()


class WorkExpirience(models.Model):
    position = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    fromtime = models.DateField()
    totime = models.DateField()
    description = models.TextField()


class KeySkills(models.Model):
    skill = models.CharField(max_length=200)


class Education(models.Model):
    institution = models.CharField(max_length=60)
    institution_website = models.URLField(max_length=60)
    faculty = models.CharField(max_length=140)
    fromtime = models.DateField()
    totime = models.DateField()
    description = models.TextField()