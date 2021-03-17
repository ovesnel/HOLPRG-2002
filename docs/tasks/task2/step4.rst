Step 4: Obtain Device's Information Dynamically
###############################################

On :ref:`t2s3` we created the interface list manually, in this step we will retrieve the information dynamically from the device using **restconf** and build a list similar to the one we built manually.

In order to complete this task, we will create a python module that retrieves information via restconf using python **requests** package.

Lets create a file named ``device.py`` inside of our ``interfaces`` application:

.. code-block:: python
    :caption: interfaces/device.py
    :linenos:

    import requests


    def get_interfaces(hostname, username, password):
        interfaces = []
        url = f"https://{hostname}/restconf/data/ietf-interfaces:interfaces/interface"

        headers = headers = {"Accept": "application/yang-data+json"}
        try:
            response = requests.request(
                "GET",
                url,
                headers=headers,
                auth=(username, password),
                verify=False,
            )

            if response.ok:
                interfaces = response.json().get("ietf-interfaces:interface", [])

        except Exception as err:
            print(f"There was an error getting interfaces: {err}")

        return interfaces


.. sectionauthor:: Luis Rueda <lurueda@cisco.com>, Jairo Leon <jaileon@cisco.com>, Ovesnel Mas Lara <omaslara@cisco.com>
