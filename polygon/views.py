from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse()


def provider(request, provider_id):
    return HttpResponse()


def provider_area(request, provider_id, area_id):
    return HttpResponse()


def provider_area_query(request, provider_id):
    return HttpResponse()


def area(request, area_id):
    return HttpResponse()


def area_query(request):
    return HttpResponse()
