from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.conf import settings

from .device import get_interfaces


def index(request):
    interface_list = get_interfaces(
        settings.DEVICE_HOST, settings.DEVICE_USER, settings.DEVICE_PASS
    )
    template = loader.get_template("interfaces/index.html")
    context = {
        "interface_list": interface_list,
    }
    return HttpResponse(template.render(context, request))
