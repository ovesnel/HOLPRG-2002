Step 2: Update view
###################

Now let’s update our interfaces/views.py to use the template:

.. code-block:: Python

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



.. sectionauthor:: Luis Rueda <lurueda@cisco.com>, Jairo Leon <jaileon@cisco.com>, Ovesnel Mas Lara <omaslara@cisco.com>
