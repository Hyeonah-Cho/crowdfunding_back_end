from django.db import models

class Fundraiser(models.Model):
    # each variable is a column in the database and its type (id is given by Django by default)
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
