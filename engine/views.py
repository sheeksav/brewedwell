from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, View
from engine.models import Brewery, Beer, Style
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

from .forms import LoginForm

# Create your views here.

class HomeView(TemplateView):
	template_name = 'engine/home.html'


class LoginView(FormView):
	form_class = LoginForm
	template_name = 'login.html'
	success_url = ''

	def get_context_data(self, **kwargs):
		context = super(LoginView, self).get_context_data(**kwargs)
		context['next'] = self.request.GET.get('next')
		return context

	def form_valid(self, form):
		username = User.objects.get(email=form.cleaned_data.get('email')).username
		user = authenticate(username=username, password=form.cleaned_data.get('password'))

		if user:
			login(self.request, user)

		if 'next' in self.request.GET:
			self.success_url = self.request.GET.next('next')
		else:
			self.success_url = '/styles/'

		return super(LoginView, self).form_valid(form)


class LogoutView(View):

	def get(self, request):
		logout(request)

		return redirect('home')


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


class BeerDetailView(TemplateView):
	template_name = 'engine/beer-detail.html'

	def dispatch(self, request, *args, **kwargs):

		try:
			beer = Beer.objects.get(pk=kwargs.get('pk'))

		except Beer.DoesNotExist:
			return redirect('beer-list')

		kwargs['beer'] = beer

		return super(BeerDetailView, self).dispatch(request, *args, **kwargs)

	def get_context_data(self, **kwargs):

		return {
			'beer': kwargs.get('beer')
		}


class StyleListView(TemplateView):
	template_name = 'engine/style-list.html'

	def get_context_data(self, **kwargs):
		style_list = Style.objects.all()
		return {
			'style_list': style_list
		}


class StyleDetailView(TemplateView):
	template_name = 'engine/style-detail.html'

	def dispatch(self, request, *args, **kwargs):

		try:
			style = Style.objects.get(pk=kwargs.get('pk'))

		except Style.DoesNotExist:
			return redirect('style-list')

		kwargs['style'] = style

		return super(StyleDetailView, self).dispatch(request, *args, **kwargs)

	def get_context_data(self, **kwargs):

		return {
			'style': kwargs.get('style'),
			'beer_list': Beer.objects.filter(style=kwargs.get('style')),
		}



