Step 3: Update View
###################

Now let’s update our interfaces/views.py to use the initial template:

.. code-block:: Python
    :linenos:
    :emphasize-lines: 20-24

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



.. sectionauthor:: Luis Rueda <lurueda@cisco.com>, Jairo Leon <jaileon@cisco.com>, Ovesnel Mas Lara <omaslara@cisco.com>
