from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='restaurants/')
    location = models.CharField(max_length=255)
    seating_capacity = models.IntegerField()
    
    def __str__(self):
        return self.name

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='hotels/')
    location = models.CharField(max_length=255)
    number_of_rooms = models.IntegerField()

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='events/')
    seating_capacity = models.IntegerField()

    def __str__(self):
        return self.name