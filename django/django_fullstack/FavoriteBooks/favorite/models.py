from django.db import models
import re

class UsersManager(models.Manager):
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

class Users(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    objects = UsersManager()


class BooksManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) == 0 :
            errors["title"] = "Title is required"
        if len(postData['description']) <= 5:
            errors["description"] = "Description must be at least 5 characters"
        return errors
    

class Books(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Users,related_name='books',on_delete=models.CASCADE)
    favorite = models.ManyToManyField(Users,related_name='favorite')
    objects = BooksManager()
