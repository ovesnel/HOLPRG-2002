Step 3: Apply Customizations to HTML Code
#########################################


.. literalinclude:: reference/table.html
    :caption: netprog/interfaces/templates/interfaces/table.html
    :language: html
    :linenos:

Create the following :guilabel:`index.html` file in the :guilabel:`netprog/interfaces/templates/interfaces/` directory:

.. literalinclude:: reference/index.html
    :caption: netprog/interfaces/templates/interfaces/index.html
    :language: html
    :linenos:

Change the interfaces application views to read the template from :guilabel:`index.html` instead of :guilabel:`table.html`:

.. literalinclude:: reference/views.py
    :caption: interfaces/views.py
    :language: python
    :linenos:
    :emphasize-lines: 11


.. sectionauthor:: Luis Rueda <lurueda@cisco.com>, Jairo Leon <jaileon@cisco.com>, Ovesnel Mas Lara <omaslara@cisco.com>
