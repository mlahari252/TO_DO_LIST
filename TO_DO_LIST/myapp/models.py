from django.db import models

# Create your models here.
class To_do(models.Model):
    task=models.CharField(max_length=200)
    desc=models.CharField(max_length=200)
    def __str__(self):
        return self.task
class To_do1(models.Model):
    task=models.CharField(max_length=300)
    desc=models.CharField(max_length=300)
    def __str__(self):
        return self.task