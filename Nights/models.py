from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from PIL import Image

class Movie(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    description = models.TextField()
    genre = models.CharField(max_length=20)
    director = models.CharField(max_length=100)
    writer = models.CharField(max_length=100)
    actors = models.CharField(max_length=200)

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        output_size = (200, 300)
        img.thumbnail(output_size)
        img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('movie-detail', kwargs={'pk': self.pk})

RATE_OPTIONS = [(1, '1-Horrrible'),
                (2, '2-Bad'),
                (3, '3-Boring'),
                (4, '4-Decent'),
                (5, '5-Good'),
                (6, '6-Grate'),
                (7, '7-Masterpiece')]

#class Review():
 #   user = models.ForeignKey(User, on_delete=models.CASCADE)
  #  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
   # rate = models.PositiveSmallIntegerField(option=RATE_OPTIONS)

