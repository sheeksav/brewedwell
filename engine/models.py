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
        (0, 'NA'),
        (1, 'Weak'),
        (2, 'Light'),
        (3, 'Moderate'),
        (4, 'Heavy'),
        (5, 'Strong'),
    )
    beer = models.ForeignKey(Beer)
    acidity = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    alcohol = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    balance = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    biscuit = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    bitter = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    body = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    bread = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    burnt = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    butter = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    caramel = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    chocolate = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    citrus = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    clove = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    coconut = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    coffee = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    crisp = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    dark_fruit = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    dry = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    earthy = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    finish = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    fruit = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    graham_cracker = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    grass = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    herbal = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    hop = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    licorice = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    malt = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    nutty = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    oak = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    pine = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    refreshing = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    resin = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    richness = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    roast = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    robust = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    salt = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    silk = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    smoke = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    sour = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    spice = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    sweet = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    syrup = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    tart = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    toast = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    toffee = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    vanilla = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    vinous = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    warmth = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    wheat = models.IntegerField(choices=FLAVOR_TAGS, default=0)
    yeast = models.IntegerField(choices=FLAVOR_TAGS, default=0)

    def __unicode__(self):
        return u'Flavor profile for %s' % self.beer.name










