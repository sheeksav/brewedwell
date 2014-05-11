from django.contrib import admin
from engine.models import Brewery, Beer, Style

# Register your models here.
admin.site.register(Brewery)
admin.site.register(Beer)
admin.site.register(Style)
