from django.urls import path
from django.conf.urls import url

from .views import view_cached_links, view_all_links, ping_pong


urlpatterns = [
    # path('search/', SearchResultsView.as_view(), name='search_results'),
    # path('', HomePageView.as_view(), name='home'),
    url(r'^cache/', view_all_links),
    url(r'^links/', view_cached_links),
    url(r'^ping/', ping_pong),
]
