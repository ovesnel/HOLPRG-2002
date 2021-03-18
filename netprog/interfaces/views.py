from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Interface
# Create your views here.


def index(request):
    interface_list = Interface.objects.all()
    template = loader.get_template("interfaces/index.html")
    context = {
        "interface_list": interface_list,
    }
    return HttpResponse(template.render(context, request))