from django.db import models

class Movies(models.Model):
    title = models.CharField(max_length=30)
    year = models.IntegerField()
    director = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)

    def __str__(self):
        return self.title