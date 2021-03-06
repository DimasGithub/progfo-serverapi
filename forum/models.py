from django.db import models

from djrichtextfield.models import RichTextField


class Tags(models.Model):
    nametags = models.CharField(primary_key=True, max_length=255)


class Groupforum(models.Model):
    namegroup = models.CharField(primary_key=True, max_length=255)
    descgroup = models.TextField()

    def __str__(self):
        return self.namegroup


class Forum(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    descproblem = RichTextField()
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE)
    group = models.ForeignKey(Groupforum, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
