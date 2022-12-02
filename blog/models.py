from django.db import models

class PopularMovie(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    title = models.CharField(max_length=200)
    

    def __str__(self):
        return self.title

class ComedyMovie(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    title = models.CharField(max_length=200)
    

    def __str__(self):
        return self.title

class ActionMovie(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    title = models.CharField(max_length=200)
    

    def __str__(self):
        return self.title