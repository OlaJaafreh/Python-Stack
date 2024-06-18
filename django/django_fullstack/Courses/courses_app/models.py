from django.db import models
import re

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) <= 5 :
            errors["name"] = "Name should be at least 5 characters"
        if len(postData['description']) <= 15:
            errors["description"] = "Description should be at least 15 characters"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    objects = CourseManager()


