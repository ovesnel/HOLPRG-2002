Step 4: Add Header And Footer
#############################

For our website to look even better, we will add the standard Cisco header and footer to our HTML templates.

The first step is to create files for our header and footer:

.. literalinclude:: reference/header.html
    :caption: interfaces/templates/interfaces/header.html
    :language: html
    :linenos:

.. literalinclude:: reference/footer.html
    :caption: interfaces/templates/interfaces/footer.html
    :language: html
    :linenos:

We will now include it in the :guilabel:`index.html`

.. literalinclude:: reference/index.html
    :caption: interfaces/templates/interfaces/index.html
    :language: html
    :linenos:
    :emphasize-lines: 12,30

Go back to your browser and refresh the http://localhost web page.

.. sectionauthor:: Ali Eftekhari <aleftekh@cisco.com>, Luis Rueda <lurueda@cisco.com>, Jairo Leon <jaileon@cisco.com>, Ovesnel Mas Lara <omaslara@cisco.com>
