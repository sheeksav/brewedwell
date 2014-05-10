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

	
