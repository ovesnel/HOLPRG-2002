Step 2: Management Interface
############################

When building our UI logic, we need to consider a special case for our management interface.
We do not want the users to be able to disable this interface.

To accomplish this, we will add logic again using the Django template language to exclude that interface from displaying an :guilabel:`Enable`/:guilabel:`Disable` button.

To simplify the logic inside our HTML code, we will add another ``if`` statement in our Django template to include a different HTML file for the interface depending on the interface name.

Let's first extract our existing logic for the ``<tr>`` (table's interface row) to a separate file named :guilabel:`interface.html` in the :guilabel:`interfaces/templates/interfaces/` directory.

.. literalinclude:: reference/interface.html
    :caption: interfaces/templates/interfaces/interface.html
    :language: html
    :linenos:

We will now create a simplified version (without the :guilabel:`Enable`/:guilabel:`Disable` button) for our management interface, we will name this file :guilabel:`management_interface.html` and it will have the following contents:

.. literalinclude:: reference/management_interface.html
    :caption: interfaces/templates/interfaces/management_interface.html
    :language: html
    :linenos:


We will now replace the ``<tr>`` inside :guilabel:`table.html` with a Django template ``if`` statement to include the file depending our interface name:

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

If we refresh our website, it will now look like this:

.. image:: images/interface-table-no-action.png
    :align: center


Pressing the :guilabel:`Enable`/:guilabel:`Disable` button will have no effect, we will add the logic for that in our next step.

.. sectionauthor:: Ali Eftekhari <aleftekh@cisco.com>, Luis Rueda <lurueda@cisco.com>, Jairo Leon <jaileon@cisco.com>, Ovesnel Mas Lara <omaslara@cisco.com>
