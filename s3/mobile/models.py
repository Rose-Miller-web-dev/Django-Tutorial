from django.db import models

# Create your models here.
class Mobile(models.Model):
    name = models.CharField(max_length=200)
    os = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    date_of_release = models.DateField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name