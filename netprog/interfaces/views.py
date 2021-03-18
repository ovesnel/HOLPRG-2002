from django.http import HttpResponse
from django.template import loader

# Create your views here.


def index(request):
    interface_list = [
        {
            "name": "GigabitEthernet1",
            "description": "Description for Gi1",
            "enabled": True,
        },
        {
            "name": "GigabitEthernet2",
            "description": "Description for Gi2",
            "enabled": False,
        },
    ]
    template = loader.get_template("interfaces/table.html")
    context = {
        "interface_list": interface_list,
    }
    return HttpResponse(template.render(context, request))