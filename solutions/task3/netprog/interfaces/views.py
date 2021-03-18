from django.http import HttpResponse
from django.template import loader

from .device import get_interfaces

# Create your views here.


def index(request):
    interface_list = get_interfaces()
    template = loader.get_template("interfaces/table.html")
    context = {
        "interface_list": interface_list,
    }
    return HttpResponse(template.render(context, request))
