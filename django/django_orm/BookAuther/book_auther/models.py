from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()

class Authors(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    notes = models.TextField()
    books = models.ManyToManyField(Books,related_name='authors')


