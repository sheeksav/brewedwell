from django.shortcuts import render
from django.views.generic import TemplateView
from engine.models import Brewery

# Create your views here.

class HomeView(TemplateView):
	template_name = 'engine/home.html'

class BreweryListView(TemplateView):
	template_name = 'engine/brewery-list.html'

	def get_context_data(self, **kwargs):
		brewery_list = Brewery.objects.all()
		return {
			'brewery_list': brewery_list
		}