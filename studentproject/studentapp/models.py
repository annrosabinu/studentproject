from django.db import models

# Create your models here.

class Student(models.Model):
    Name=models.CharField(max_length=255,null=True)
    address=models.TextField()
    age=models.CharField(max_length=255)
    email=models.EmailField()
    joinIngdate=models.DateField()
    qualification=models.CharField(max_length=255,null=True)
    gender=models.CharField(max_length=255)
    mobileno=models.CharField(max_length=255)