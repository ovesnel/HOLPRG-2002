Step 1: Create the HTML template
################################

Let's create a :guilabel:`table.html` file in the :guilabel:`netprog/interfaces/templates/interfaces` directory (you have to create the directories), with the following content:

.. literalinclude:: reference/table.html
    :caption: netprog/interfaces/templates/interfaces/table.html
    :language: html
    :linenos:

.. note::
    The above html uses Django template language, which includes a for loop.
    This basically means that Django will walk through the ``interface_list`` python list and will create the enclosed ``HTML`` for each element in the list.

.. sectionauthor:: Luis Rueda <lurueda@cisco.com>, Jairo Leon <jaileon@cisco.com>, Ovesnel Mas Lara <omaslara@cisco.com>
