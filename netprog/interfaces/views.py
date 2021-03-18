from django.shortcuts import render
from django.http import HttpResponse

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
    return HttpResponse(str(interface_list))