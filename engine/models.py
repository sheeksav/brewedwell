from django.db import models

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
	abv = models.FloatField(null=True)
	ibu = models.FloatField(null=True)
	srm = models.FloatField(null=True)

	def __unicode__(self):
		return self.name



