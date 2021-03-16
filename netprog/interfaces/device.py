import json
import re
import requests


def interface_split(interface):
    return list(filter(None, re.split(r"(\d+)", interface)))


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


def disable_interface(interface, hostname, username, password):
    interface_full = interface_split(interface)
    interface_type = interface_full[0]
    interface_number = interface_full[1]
    url = f"https://{hostname}/restconf/data/Cisco-IOS-XE-native:native/interface/{interface_type}={interface_number}"
    headers = headers = {"Content-type": "application/yang-data+json"}
    payload = {f"Cisco-IOS-XE-native:{interface_type}": {"shutdown": [None]}}
    try:
        response = requests.request(
            "PATCH",
            url,
            data=json.dumps(payload),
            headers=headers,
            auth=(username, password),
            verify=False,
        )

        if response.ok:
            return True

    except Exception as err:
        print(f"There was an error disabling interface: {err}")
        return False


def enable_interface(interface, hostname, username, password):
    interface_full = interface_split(interface)
    interface_type = interface_full[0]
    interface_number = interface_full[1]
    url = f"https://{hostname}/restconf/data/Cisco-IOS-XE-native:native/interface/{interface_type}={interface_number}"
    headers = headers = {
        "Accept": "application/yang-data+json",
        "Content-type": "application/yang-data+json",
    }
    try:

        response = requests.request(
            "GET",
            url,
            headers=headers,
            auth=(username, password),
            verify=False,
        )

        if response.ok:
            payload = response.json()
            details = payload.pop(f"Cisco-IOS-XE-native:{interface_type}", None)

            if details:
                details.pop("shutdown", None)
                payload[f"Cisco-IOS-XE-native:{interface_type}"] = details

        response = requests.request(
            "PUT",
            url,
            data=json.dumps(payload),
            headers=headers,
            auth=(username, password),
            verify=False,
        )

        if response.ok:
            return True

    except Exception as err:
        print(f"There was an error enabling interface: {err}")
        return False


def get_interfaces(hostname, username, password):
    interfaces = []
    url = f"https://{hostname}/restconf/data/Cisco-IOS-XE-native:native/interface"

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
            interfaces = convert_interface_object(response.json())

    except Exception as err:
        print(f"There was an error getting interfaces: {err}")

    return interfaces
