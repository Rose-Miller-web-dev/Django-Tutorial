from django.db import models

# Create your models here.

class Singer(models.Model):
    name = models.CharField(max_length=200)
    sure_name = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200)
    birth = models.DateField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=200)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
    year_of_release = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
