from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=45)


class Actor(models.Model):
    name = models.CharField(max_length=45)

class Movie(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    url_img = models.TextField()
    cat = models.ForeignKey(Category,related_name='movies',on_delete=models.CASCADE)
    act = models.ManyToManyField(Actor,related_name='movies')

class Movie_has_Actor(models.Model):
    act = models.ForeignKey(Actor,related_name='actmovie',on_delete=models.CASCADE)
    count = models.IntegerField(default=0)


