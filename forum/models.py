from django.db import models
from ckeditor.fields import RichTextField


class Tags(models.Model):
    nametags = models.CharField(primary_key=True, max_length=255)

    def __str__(self):
        return self.nametags


class Groupforum(models.Model):
    namegroup = models.CharField(primary_key=True, max_length=255)
    descgroup = models.TextField()

    def __str__(self):
        return self.namegroup


class Forum(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    descproblem = RichTextField()
    tags = models.ManyToManyField(Tags)
    group = models.ForeignKey(Groupforum, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
