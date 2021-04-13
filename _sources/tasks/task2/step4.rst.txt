Step 4: Obtain Device's Information Dynamically
###############################################

On :ref:`t2s3` we created the interface list manually, in this step we will retrieve the information dynamically from the device using **restconf** and build a list similar to the one we built manually.

To complete this task, we will create a python module that retrieves information via restconf using python **requests** package.

Let's create a file named :guilabel:`device.py` inside of our :guilabel:`netprog/interfaces` application directory:

.. literalinclude:: reference/device.py
    :caption: netprog/interfaces/device.py
    :language: python
    :linenos:


We can now run this module within the container to test that we can fetch interfaces information from the device using **restconf**:

.. code-block:: bash

    python interfaces/device.py 

You should get an output similar to the one shown below with the interfaces information encoded in JSON format: 

.. code-block:: bash
    :emphasize-lines: 4

    root@c22887e81072:/app# python interfaces/device.py 
    /usr/local/lib/python3.9/site-packages/urllib3/connectionpool.py:1013: InsecureRequestWarning: Unverified HTTPS request is being made to host '198.18.134.11'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
    warnings.warn(
    [{'name': 'GigabitEthernet1', 'type': 'iana-if-type:ethernetCsmacd', 'enabled': True, 'ietf-ip:ipv4': {'address': [{'ip': '198.18.134.11', 'netmask': '255.255.192.0'}]}, 'ietf-ip:ipv6': {}}, {'name': 'GigabitEthernet2', 'description': 'This is GigabitEthernet 2', 'type': 'iana-if-type:ethernetCsmacd', 'enabled': False, 'ietf-ip:ipv4': {}, 'ietf-ip:ipv6': {}}]


Update :guilabel:`views.py` to use the fuction to get interfaces infomation dynamically.

.. literalinclude:: reference/views.py
    :caption: netprog/interfaces/views.py
    :language: python
    :linenos:
    :emphasize-lines: 4,10

Go back to your browser and refresh the http://localhost web page.
You should see the interfaces information in **JSON** format.

.. TODO:: 
    Add image for refreshed web page

.. sectionauthor:: Ali Eftekhari <aleftekh@cisco.com>, Luis Rueda <lurueda@cisco.com>, Jairo Leon <jaileon@cisco.com>, Ovesnel Mas Lara <omaslara@cisco.com>
