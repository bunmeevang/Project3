from django.db import models

class Array(models.Model):
    author = models.CharField(max_length=100)
    body = models.CharField(max_length=3000)



class Push(models.Model):
    author = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
    array = models.ForeignKey(Array, on_delete=models.CASCADE, related_name="pushes")