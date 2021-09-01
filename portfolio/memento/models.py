from django.db import models


class Project(models.Model):
    image = models.ImageField(upload_to="media")
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=500)
    technology = models.CharField(max_length=200)

    def __str__(self):
        return self.title
