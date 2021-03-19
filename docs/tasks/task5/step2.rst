Step 2: Management Interface
############################

When building our UI logic, we need to consider a special case for our management interface.
We do not want the users to be able to disable this interface.

To accomplish this, we will add logic again using Django template language.z
To exclude that interface from displaying an :guilabel:`Enable`/:guilabel:`Disable` button.

Let's first extract our existing logic for the ``<tr>`` (table's interface row) to a separate file named :guilabel:`interface.html`


.. literalinclude:: reference/interface.html
    :caption: interfaces/templates/interfaces/interface.html
    :language: html
    :linenos:
    :emphasize-lines: 11


To simplify the logic inside our HTML code, we will add another ``if`` statement in our Django template to include a different HTML file for the interface depending on the interface name:

.. code-block:: html
    :caption: interfaces/templates/interfaces/table.html
    :emphasize-lines: 3-7

    {% for interface in interface_list %}
    <tr>
        {% if interface.name == "GigabitEthernet1" %}
        {% include "./management_interface.html" %}
        {% else %}
        {% include "./interface.html" %}
        {% endif %}
    </tr>
    {% endfor %}


.. sectionauthor:: Luis Rueda <lurueda@cisco.com>, Jairo Leon <jaileon@cisco.com>, Ovesnel Mas Lara <omaslara@cisco.com>
