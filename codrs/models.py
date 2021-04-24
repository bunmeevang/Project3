from django.db import models

class Array(models.Model):
    user = models.CharField(max_length=100, default='')
    body = models.CharField(max_length=3000, default='')

class Push(models.Model):
    user = models.CharField(max_length=100, default='')
    push = models.CharField(max_length=1000, default='')
    array = models.ForeignKey(Array, on_delete=models.CASCADE, related_name="push")

class Profile(models.Model):
    firstname = models.CharField(max_length=100, default='')
    lastname = models.CharField(max_length=100, default='')
    genderpronouns = models.CharField(max_length=100, default='')
    location = models.CharField(max_length=100, default='')
    aboutme = models.CharField(max_length=500, default='')
    linkedin = models.CharField(max_length=100, default='')