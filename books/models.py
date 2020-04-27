from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField()
    published_at = models.DateField()

    author = models.CharField(null=True, max_length=128) # nowe

    def __str__(self):
        return "ksiażka: " + self.title