from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=127, unique=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=127)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    genre = models.ManyToManyField(Genre)
    url = models.URLField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.FloatField(null=True)
    review = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.movie.title