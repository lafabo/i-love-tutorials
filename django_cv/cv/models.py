from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    mail = models.EmailField(blank=True)
    phone = models.CharField(max_length=12, blank=True)
    website = models.URLField(verbose_name='Homepage url', blank=True)
    skype = models.CharField(max_length=30, blank=True)
    summary = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photo/', blank=True)

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % self.photo)


class Experience(models.Model):
    ref = models.ForeignKey(Person, related_name='work', default=1)
    position = models.CharField(max_length=30)
    company = models.CharField(max_length=30, blank=True)
    fromtime = models.DateField()
    totime = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)


class KeySkills(models.Model):
    ref = models.ForeignKey(Person, related_name='skills', default=1)
    skill = models.CharField(max_length=200)


class Education(models.Model):
    ref = models.ForeignKey(Person, related_name='edu', default=1)
    institution = models.CharField(max_length=60)
    institution_website = models.URLField(max_length=60, blank=True)
    faculty = models.CharField(max_length=140)
    fromtime = models.DateField()
    totime = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
