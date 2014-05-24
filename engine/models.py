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
        return u'%s %s %s' % (self.user.first_name, self.choice, self.beer.name)


class Flavor(models.Model):
    FLAVOR_TAGS = (
        ('0', 'Weak'),
        ('1', 'Light'),
        ('2', 'Moderate'),
        ('3', 'Heavy'),
        ('4', 'Strong'),
    )
    beer = models.ForeignKey(Beer)
    acidity = models.IntegerField(choices=FLAVOR_TAGS)
    alcohol = models.IntegerField(choices=FLAVOR_TAGS)
    balance = models.IntegerField(choices=FLAVOR_TAGS)
    biscuit = models.IntegerField(choices=FLAVOR_TAGS)
    bitter = models.IntegerField(choices=FLAVOR_TAGS)
    body = models.IntegerField(choices=FLAVOR_TAGS)
    bread = models.IntegerField(choices=FLAVOR_TAGS)
    burnt = models.IntegerField(choices=FLAVOR_TAGS)
    butter = models.IntegerField(choices=FLAVOR_TAGS)
    caramel = models.IntegerField(choices=FLAVOR_TAGS)
    chocolate = models.IntegerField(choices=FLAVOR_TAGS)
    citrus = models.IntegerField(choices=FLAVOR_TAGS)
    clove = models.IntegerField(choices=FLAVOR_TAGS)
    coconut = models.IntegerField(choices=FLAVOR_TAGS)
    coffee = models.IntegerField(choices=FLAVOR_TAGS)
    crisp = models.IntegerField(choices=FLAVOR_TAGS)
    dark_fruit = models.IntegerField(choices=FLAVOR_TAGS)
    dry = models.IntegerField(choices=FLAVOR_TAGS)
    earthy = models.IntegerField(choices=FLAVOR_TAGS)
    finish = models.IntegerField(choices=FLAVOR_TAGS)
    fruit = models.IntegerField(choices=FLAVOR_TAGS)
    graham_cracker = models.IntegerField(choices=FLAVOR_TAGS)
    grass = models.IntegerField(choices=FLAVOR_TAGS)
    herbal = models.IntegerField(choices=FLAVOR_TAGS)
    hop = models.IntegerField(choices=FLAVOR_TAGS)
    licorice = models.IntegerField(choices=FLAVOR_TAGS)
    malt = models.IntegerField(choices=FLAVOR_TAGS)
    nutty = models.IntegerField(choices=FLAVOR_TAGS)
    oak = models.IntegerField(choices=FLAVOR_TAGS)
    pine = models.IntegerField(choices=FLAVOR_TAGS)
    refreshing = models.IntegerField(choices=FLAVOR_TAGS)
    resin = models.IntegerField(choices=FLAVOR_TAGS)
    richness = models.IntegerField(choices=FLAVOR_TAGS)
    roast = models.IntegerField(choices=FLAVOR_TAGS)
    robust = models.IntegerField(choices=FLAVOR_TAGS)
    salt = models.IntegerField(choices=FLAVOR_TAGS)
    silk = models.IntegerField(choices=FLAVOR_TAGS)
    smoke = models.IntegerField(choices=FLAVOR_TAGS)
    sour = models.IntegerField(choices=FLAVOR_TAGS)
    spice = models.IntegerField(choices=FLAVOR_TAGS)
    sweet = models.IntegerField(choices=FLAVOR_TAGS)
    syrup = models.IntegerField(choices=FLAVOR_TAGS)
    tart = models.IntegerField(choices=FLAVOR_TAGS)
    toast = models.IntegerField(choices=FLAVOR_TAGS)
    toffee = models.IntegerField(choices=FLAVOR_TAGS)
    vanilla = models.IntegerField(choices=FLAVOR_TAGS)
    vinous = models.IntegerField(choices=FLAVOR_TAGS)
    warmth = models.IntegerField(choices=FLAVOR_TAGS)
    wheat = models.IntegerField(choices=FLAVOR_TAGS)
    yeast = models.IntegerField(choices=FLAVOR_TAGS)








