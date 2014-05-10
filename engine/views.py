from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from engine.models import Brewery, Beer

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


class BeerListView(TemplateView):
	template_name = 'engine/beer-list.html'

	def get_context_data(self, **kwargs):
		beer_list = Beer.objects.all()
		return {
			'beer_list': beer_list
		}

class BreweryDetailView(TemplateView):
	template_name = 'engine/brewery-detail.html'

	def dispatch(self, request, *args, **kwargs):

		try:
			brewery = Brewery.objects.get(pk=kwargs.get('pk'))

		except Brewery.DoesNotExist:
			return redirect('brewery-list')

		kwargs['brewery'] = brewery

		return super(BreweryDetailView, self).dispatch(request, *args, **kwargs)

	def get_context_data(self, **kwargs):

		return {
			'brewery': kwargs.get('brewery'),
			'beer_list': Beer.objects.filter(brewery=kwargs.get('brewery')),
		}

