import json
import re
import requests


def set_interface(interface, enabled, hostname, username, password):
    print(f"Setting interface '{interface}' to enabled: '{enabled}'")
    url = f"https://{hostname}/restconf/data/ietf-interfaces:interfaces"
    headers = headers = {
        "Accept": "application/yang-data+json",
        "Content-type": "application/yang-data+json",
    }
    payload = {
        "ietf-interfaces:interfaces": {
            "interface": {"name": interface, "enabled": enabled}
        }
    }
    try:
        response = requests.request(
            "PATCH",
            url,
            data=json.dumps(payload),
            headers=headers,
            auth=(username, password),
            verify=False,
        )

    except Exception as err:
        print(f"There was an error setting interface '{interface}': {err}")


def get_interfaces(hostname, username, password):
    interfaces = []
    url = f"https://{hostname}/restconf/data/ietf-interfaces:interfaces"

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
            interfaces = (
                response.json()
                .get("ietf-interfaces:interfaces", {})
                .get("interface", [])
            )

    except Exception as err:
        print(f"There was an error getting interfaces: {err}")

    return interfaces
