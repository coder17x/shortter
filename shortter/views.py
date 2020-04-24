import json

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

from .models import Links

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@api_view(['GET'])
def ping_pong(request):
    results = json.dumps("Pong!")
    return Response(results, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def view_all_links(request):
    results = {"status": "Error", }
    if request.method == "GET":
        links = Links.objects.all()
        results.update({"status": "success", "links": [link.to_json() for link in links]})
    elif request.method == "POST":
        results.update({"message": "not implemented"})

    return Response(results, status=status.HTTP_200_OK)


@api_view(['GET'])
def view_cached_links(request):
    results = {"status": "Error", }
    if 'link' in cache:
        # get results from cache
        links = cache.get('link')
        results.update({"status": "success", "links": [link.to_json() for link in links]})
        return Response(results, status=status.HTTP_201_CREATED)

    else:
        links = Links.objects.all()
        result = [link.to_json() for link in links]
        # store data in cache
        cache.set(links, result, timeout=CACHE_TTL)
        results.update({"status": "success", "links": result})
        return Response(results, status=status.HTTP_201_CREATED)
