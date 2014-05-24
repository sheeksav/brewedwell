from django.conf.urls import patterns, include, url
from engine.views import HomeView, BreweryListView, BeerListView, BreweryDetailView, BeerDetailView, StyleListView, \
StyleDetailView, LoginView, LogoutView, SignupView, WishListView, LikeBeerView, SaveBeerView, DislikeBeerView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'brewedwell.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^signup/$', SignupView.as_view(), name='signup'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^breweries/$', BreweryListView.as_view(), name='brewery-list'),
    url(r'^beers/$', BeerListView.as_view(), name='beer-list'),
    url(r'^breweries/(?P<pk>\d+)/$', BreweryDetailView.as_view(), name='brewery-detail'),
    url(r'^beers/(?P<pk>\d+)/$', BeerDetailView.as_view(), name='beer-detail'),
    url(r'^styles/$', StyleListView.as_view(), name='style-list'),
    url(r'^styles/(?P<pk>\d+)/$', StyleDetailView.as_view(), name='style-detail'),
    url(r'^wishlist/$', WishListView.as_view(), name='wishlist'),
    url(r'^beers/like/(?P<pk>\d+)/$', LikeBeerView, name='like-beer'),
    url(r'^beers/save/(?P<pk>\d+)/$', SaveBeerView, name='save-beer'),
    url(r'^beers/dislike/(?P<pk>\d+)/$', DislikeBeerView, name='dislike-beer'),
)
