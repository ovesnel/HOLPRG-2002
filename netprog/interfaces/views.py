from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.conf import settings

from .device import disable_interface, enable_interface, get_interfaces


def index(request):
    if request.method == "POST":
        desired_state = request.POST.dict()
        print(desired_state)
        interface_to_enable = desired_state.get("enable")
        interface_to_disable = desired_state.get("disable")

        if interface_to_enable:
            enable_interface(
                interface_to_enable,
                settings.DEVICE_HOST,
                settings.DEVICE_USER,
                settings.DEVICE_PASS,
            )

        if interface_to_disable:
            disable_interface(
                interface_to_disable,
                settings.DEVICE_HOST,
                settings.DEVICE_USER,
                settings.DEVICE_PASS,
            )

    interface_list = get_interfaces(
        settings.DEVICE_HOST, settings.DEVICE_USER, settings.DEVICE_PASS
    )
    template = loader.get_template("interfaces/index.html")
    context = {
        "interface_list": interface_list,
    }
    return HttpResponse(template.render(context, request))
