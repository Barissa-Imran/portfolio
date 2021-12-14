from django.db import models
from django.db.models.fields import URLField
from phonenumber_field.modelfields import PhoneNumberField


class Project(models.Model):
    image = models.ImageField(upload_to="media")
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=500)
    technology = models.CharField(max_length=200)
    source_code = models.URLField(default="https://github.com/Barissa-Imran")
    demo = models.URLField(default="https://github.com/Barissa-Imran")

    def __str__(self):
        return self.title


# from top of the cv left to right...
class Resume(models.Model):
    CV = models.FileField(upload_to="cv")


class Education(models.Model):
    institution = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    area_of_focus = models.TextField()

    def __str__(self):
        return self.institution


class Experience(models.Model):
    company = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)
    responsibilities = models.TextField()

    def __str__(self):
        return self.company


class RelevantCourses(models.Model):
    institution = models.CharField(max_length=200)
    study = models.CharField(max_length=200)

    def __str__(self):
        return self.study


class Leadership(models.Model):
    institution = models.CharField(max_length=200)
    award = models.CharField(max_length=200)

    def __str__(self):
        return self.award


class Referee(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    organisation = models.CharField(max_length=200)
    address = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField()
    tel = PhoneNumberField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return self.email
