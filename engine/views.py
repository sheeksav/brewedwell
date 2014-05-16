from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, View
from engine.models import Brewery, Beer, Style
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, SignupForm

# Create your views here.


class HomeView(TemplateView):
	template_name = 'engine/home.html'


class SignupView(FormView):
	form_class = SignupForm
	template_name = 'signup.html'
	success_url = '/styles/'

	def form_valid(self, form):

		# Get data from form
		email = form.cleaned_data.get('email').lower()
		username = email[:30] # Limit to 30 chars
		first_name = form.cleaned_data.get('first_name')
		last_name = form.cleaned_data.get('last_name')
		password = form.cleaned_data.get('password')

		# Create a new user object
		user = User.objects.create_user(username=username, email=email, password= password, first_name=first_name, last_name=last_name)

		# Authenticate the user
		user = authenticate(username=username, password=password)

		# Log the user in
		login(self.request, user)

		return super(SignupView, self).form_valid(form)


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
			self.success_url = self.request.GET.get('next')
		else:
			self.success_url = '/styles/'

		return super(LoginView, self).form_valid(form)


class LogoutView(View):

	def get(self, request):
		logout(request)

		return redirect('home')


class BreweryListView(TemplateView):
	template_name = 'engine/brewery-list.html'

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):

		return super(BreweryListView, self).dispatch(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		brewery_list = Brewery.objects.all()
		return {
			'brewery_list': brewery_list
		}


class BeerListView(TemplateView):
	template_name = 'engine/beer-list.html'

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):

		return super(BeerListView, self).dispatch(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		beer_list = Beer.objects.all()
		return {
			'beer_list': beer_list
		}


class BreweryDetailView(TemplateView):
	template_name = 'engine/brewery-detail.html'

	@method_decorator(login_required)
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

	@method_decorator(login_required)
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

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):

		return super(StyleListView, self).dispatch(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		
		style_list = Style.objects.all()
		return {
			'style_list': style_list
		}



class StyleDetailView(TemplateView):
	template_name = 'engine/style-detail.html'

	@method_decorator(login_required)
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



