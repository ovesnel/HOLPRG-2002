Step 1: Add Enable/Disable Interface Button
###########################################


We will now add a button to enable/disable the interface.
Initially our button will not execute any actions in the backend.
We will later add the code to execute an action when the button is clicked.

We will begin by adding and extra column in our table that will contain the :guilabel:`Enable`/:guilabel:`Disable` button.

In our :guilabel:`interfaces/templates/interfaces/table.html` let's add the column by inserting another ``<th>``.
The following code should be used:

.. code-block:: html
    :caption: interfaces/templates/interfaces/table.html
    :emphasize-lines: 5

    <tr>
        <th>Name</th>
        <th>Description</th>
        <th class="text-center">Enabled</th>
        <th class="text-center">Action</th>
    </tr>

We also have to add another row in our for loop and inside the existing condition for enabled/disabled, we will add an HTML button.
The button will be different when the interface is **enabled** than when it is **disabled**.

The following code, shows what needs to be added:

.. code-block:: html
    :caption: interfaces/templates/interfaces/table.html
    :emphasize-lines: 7-9,12-14

    {% for interface in interface_list %}
    <tr>
        <td>{{ interface.name }}</td>
        <td>{{ interface.description }}</td>
        {% if interface.enabled %}
        <td class="text-center"><span class="icon-check text-success"></span></td>
        <td class="text-center">
            <button class="btn btn--small btn--danger" value="{{ interface.name }}" name="disable">Disable</button>
        </td>
        {% else %}
        <td class="text-center"><span class="icon-close text-danger"></span></td>
        <td class="text-center">
            <button class="btn btn--small btn--success" value="{{ interface.name }}" name="enable">Enable</button>
        </td>
        {% endif %}
    </tr>
    {% endfor %}


.. sectionauthor:: Ali Eftekhari <aleftekh@cisco.com>, Luis Rueda <lurueda@cisco.com>, Jairo Leon <jaileon@cisco.com>, Ovesnel Mas Lara <omaslara@cisco.com>
