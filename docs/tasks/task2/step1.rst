Step 1: Determining Data Structure
##################################

The first step is to determine the data structure for the device's interfaces.

We will use **Postman** to connect to the device and obtain information about the interfaces.

Open **Postman**, click :guilabel:`Import` then select :guilabel:`Folder` tab and choose the folder :guilabel:`HOLPRG-2002/postman/` finally click the :guilabel:`Import` button to import the collection.

You should see a collection called **CL2021-HOLPRG-2002**, under this collection select the option :guilabel:`GET Interfaces` and click the :guilabel:`Send` button.

From the body of the response we obtain the following structure:

.. code-block:: json

   {
      "ietf-interfaces:interface": [
         {
               "name": "GigabitEthernet1",
               "type": "iana-if-type:ethernetCsmacd",
               "enabled": true,
               "ietf-ip:ipv4": {
                  "address": [
                     {
                           "ip": "198.18.134.11",
                           "netmask": "255.255.192.0"
                     }
                  ]
               },
               "ietf-ip:ipv6": {}
         },
         {
               "name": "GigabitEthernet2",
               "description": "This is GigabitEthernet 2",
               "type": "iana-if-type:ethernetCsmacd",
               "enabled": false,
               "ietf-ip:ipv4": {},
               "ietf-ip:ipv6": {}
         }
      ]
   }


From the above output, we have an array of interfaces with the following relevant keys:

- name
- description
- enabled


.. sectionauthor:: Ali Eftekhari <aleftekh@cisco.com>, Luis Rueda <lurueda@cisco.com>, Jairo Leon <jaileon@cisco.com>, Ovesnel Mas Lara <omaslara@cisco.com>
