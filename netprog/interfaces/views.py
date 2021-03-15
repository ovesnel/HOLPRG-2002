from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Page under construction! You're at the Device Interfaces index.")
