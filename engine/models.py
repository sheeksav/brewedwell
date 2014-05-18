from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Brewery(models.Model):
    name = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Breweries"

    def __unicode__(self):
        return self.name


class Style(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=2000, default="No description provided.")

    def __unicode__(self):
        return self.name


class Beer(models.Model):
    brewery = models.ForeignKey(Brewery)
    name = models.CharField(max_length=300)
    style = models.ForeignKey(Style, null=True)
    description = models.CharField(max_length=2000, default="No description provided.")
    abv = models.FloatField(null=True, blank=True)
    ibu = models.FloatField(null=True, blank=True)
    srm = models.FloatField(null=True, blank=True)
    likes = models.IntegerField(default=0)
    saves = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class History(models.Model):
    HISTORY_CHOICES = (
        ('LI', 'Liked'),
        ('DL', 'Disliked'),
        ('SA', 'Saved'),
    )
    choice = models.CharField(max_length=2, choices=HISTORY_CHOICES)
    beer = models.ForeignKey(Beer)
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "History Items"

    def __unicode__(self):
        return self.name





