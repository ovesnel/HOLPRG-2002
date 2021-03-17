Step 1: Determining Data Structure
##################################

The first step is to determine the data structure for the device's interfaces.

In order to do so, we will use postman to connect to the device and obtain information about the interfaces.

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

We want to take this information and build a table like the specified below:

.. csv-table::
   :file: ./reference/interfaces.csv
   :width: 80%
   :header-rows: 1


.. sectionauthor:: Luis Rueda <lurueda@cisco.com>, Jairo Leon <jaileon@cisco.com>, Ovesnel Mas Lara <omaslara@cisco.com>
