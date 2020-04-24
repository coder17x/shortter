from django.conf.urls import url

from .views import view_cached_links, view_all_links


urlpatterns = [
    url(r'^cache/', view_all_links),
    url(r'^links/', view_cached_links),
]
