from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    restaurant_rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Review(models.Model):
    restaurant = models.ForeignKey('Restaurant')
    review = models.TextField()
    user = models.ForeignKey(User)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s review: %s..." % (self.restaurant, self.review[:20])

class Rating(models.Model):
    restaurant = models.ForeignKey('Restaurant')
    user = models.ForeignKey(User)
    RESTAURANT_RATING_CHOICES = (
        (1, 'Poor'),
        (2, 'Unsatisfactory'),
        (3, 'Average'),
        (4, 'Good'),
        (5, 'Excellent'),
    )
    rating = models.IntegerField(default=3, choices=RESTAURANT_RATING_CHOICES)

    def __str__(self):
        return "%s: %s" % (self.restaurant, self.user)
