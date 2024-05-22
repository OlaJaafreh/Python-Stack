from django.db import models
from datetime import date



class TVShowsManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if date.fromisoformat(postData['releasedate']) > date.today():
            errors["releasedate"] = "Ensure the Release Date is in the past"
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if len(postData['network']) < 2:
            errors["network"] = "Network should be at least 2 characters"
        if len(postData['description']) !=0 and len(postData['description']) < 10:
            errors["description"] = "Blog description should be at least 10 characters"
        return errors




class TVShows(models.Model):
    title =models.CharField(max_length=45)
    network =models.CharField(max_length=45)
    releasedate = models.DateField()
    description = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    objects = TVShowsManager()


