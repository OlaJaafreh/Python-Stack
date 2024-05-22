from django.db import models

class TVShows(models.Model):
    title =models.CharField(max_length=45)
    network =models.CharField(max_length=45)
    releasedate = models.DateField()
    description = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
