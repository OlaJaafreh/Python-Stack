from django.db import models
import re
import bcrypt

class RegManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        Name_REGEX = re.compile(r'^[a-zA-Z]+$')
        if len(postData['first_name']) <= 2 or not Name_REGEX.match(postData['first_name']):
            errors["first_name"] = "Name should be at least 2 characters"
        if len(postData['last_name']) <= 2:
            errors["last_name"] = "Name should be at least 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):   
            errors['email'] = "Invalid email address!"
        if len(postData['password']) <= 8:
            errors["password"] = "password should be at least 8 characters"
        if  postData['password'] != postData['Confirmpassword']:
            errors["Confirmpassword"] = "password didnt match"
        return errors
    

class LogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not Registration.objects.filter(email=postData['emailLog']).exists():
            errors["emailLog"] = "Email not found"
        elif not EMAIL_REGEX.match(postData['emailLog']):   
            errors['emailLog'] = "Invalid email address!"
        elif not bcrypt.checkpw(postData['pass'].encode(), Registration.objects.get(email= postData['emailLog']).password.encode()):
            errors["pass"] = "password incorrect"
        return errors

class Registration(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects=RegManager()

class LogIn(models.Model):
    objects=LogManager()


