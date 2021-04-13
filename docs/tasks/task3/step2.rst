Step 2: Update View To Use The HTML Template
############################################

Now let’s update our :guilabel:`netprog/interfaces/views.py` to use the initial template:

.. literalinclude:: reference/views.py
    :caption: netprog/interfaces/views.py
    :language: python
    :linenos:
    :emphasize-lines: 2,11-15

Go back to your browser and refresh the http://localhost web page.
You should now see the device's interfaces in the form of an HTML table.

.. image:: images/interfaces-table-view.png
    :align: center

.. sectionauthor:: Ali Eftekhari <aleftekh@cisco.com>, Luis Rueda <lurueda@cisco.com>, Jairo Leon <jaileon@cisco.com>, Ovesnel Mas Lara <omaslara@cisco.com>
