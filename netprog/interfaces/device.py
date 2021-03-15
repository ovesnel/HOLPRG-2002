import requests
from requests.auth import HTTPBasicAuth


def convert_interface_object(interface_object):
    interfaces = []
    for interface_type in interface_object["Cisco-IOS-XE-native:interface"].keys():
        for interface_details in interface_object["Cisco-IOS-XE-native:interface"][
            interface_type
        ]:
            shutdown = False
            if interface_details.get("shutdown", False):
                shutdown = True
            interfaces.append(
                {
                    "name": f"{interface_type}{interface_details['name']}",
                    "description": interface_details.get("description", ""),
                    "shutdown": shutdown,
                }
            )
    return interfaces


def get_interfaces(hostname, username, password):
    interfaces = []
    url = f"https://{hostname}/restconf/data/Cisco-IOS-XE-native:native/interface"

    headers = headers = {"Accept": "application/yang-data+json"}
    try:
        response = requests.request(
            "GET",
            url,
            headers=headers,
            auth=HTTPBasicAuth(username, password),
            verify=False,
        )

        if response.ok:
            interfaces = convert_interface_object(response.json())

    except Exception as err:
        print(f"There was an error getting interfaces: {err}")

    return interfaces
