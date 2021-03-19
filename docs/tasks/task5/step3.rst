Step 3: Add Logic To Enable/Disable Button
##########################################

the first step is to wrap our table into an HTML form:

.. literalinclude:: reference/table.html
    :caption: interfaces/templates/interfaces/table.html
    :language: html
    :emphasize-lines: 1-2,22
    :linenos:
    
.. note::
    
    The ``csrf_token`` template tag provides easy-to-use protection against `Cross Site Request Forgeries attacks <https://www.squarefree.com/securitytips/web-developers.html#CSRF>`__.

Now that our HTML behaves as a form, we will now have to add the relevant code inside our view to take an action when the form is submitted.

Let's add another function to our :guilabel:`device.py` that changes the interface in our backed when invoked:

.. literalinclude:: reference/device.py
    :caption: interfaces/device.py
    :language: python
    :emphasize-lines: 1,5-29
    :linenos:

When our form is submitted we will call the new ``set_interface()`` function with the relevant parameters:

.. literalinclude:: reference/views.py
    :caption: interfaces/views.py
    :language: python
    :emphasize-lines: 4,10-19
    :linenos:

If we refresh our website, now our button does have an action and should enable or disable the interface when pressed!

.. sectionauthor:: Luis Rueda <lurueda@cisco.com>, Jairo Leon <jaileon@cisco.com>, Ovesnel Mas Lara <omaslara@cisco.com>
