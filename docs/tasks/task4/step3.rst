Step 3: Apply Customizations to HTML Code
#########################################


.. literalinclude:: reference/table.html
    :caption: interfaces/templates/interfaces/table.html
    :language: html
    :linenos:

.. literalinclude:: reference/index.html
    :caption: interfaces/templates/interfaces/index.html
    :language: html
    :linenos:

Change the views to read from ``index.html`` instead of ``table.html``

.. literalinclude:: reference/views.py
    :caption: interfaces/views.py
    :language: python
    :linenos:
    :emphasize-lines: 11


.. sectionauthor:: Luis Rueda <lurueda@cisco.com>, Jairo Leon <jaileon@cisco.com>, Ovesnel Mas Lara <omaslara@cisco.com>
