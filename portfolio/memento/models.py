from enum import unique
from django.db import models

# Create your models here.
class Project(models.Model):
    image = models.ImageField(upload_to="projects")
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=250)
    technology = models.CharField(max_length=200)

    def __str__(self):
        return self.title