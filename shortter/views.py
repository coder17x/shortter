from django.shortcuts import render

from django.views.generic import TemplateView, ListView
from django.db.models import Q

from .models import Links


class HomePageView(TemplateView):
    template_name = 'home.html'


class SearchResultsView(ListView):
    model = Links
    template_name = 'search_results.html'

    def get_queryset(self): # новый
        query = self.request.GET.get('q')
        object_list = Links.objects.filter(
            Q(lnk_full_name__icontains=query) | Q(lnk_short_name__icontains=query)
        )
        return object_list
