from django.shortcuts import render
from django.http import HttpResponse


def main_page(request):
    return HttpResponse('<h4>Abracodabra</h4>')
