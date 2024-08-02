from django.db import models


class Review(models.Model):
    s = [('publish', 'publish'), ('not publish', 'not publish')]
    g = [('action', 'action'), ('thriller', 'thriller'), ('horror', 'horror'), ('sci-fi', 'sci-fi'), ('comedy', 'comedy')]
    r_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    rating = models.IntegerField()
    created_at = models.DateField()
    email = models.EmailField()
    status = models.CharField(max_length=50, choices=s)
    genres = models.CharField(max_length=50, choices=g)
