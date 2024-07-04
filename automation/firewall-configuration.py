import requests
from config import PFSENSE_API_URL, PFSENSE_API_KEY

headers = {
    'Authorization': f'Bearer {PFSENSE_API_KEY}',
    'Content-Type': 'application/json'
}

def add_firewall_rule(action, interface, protocol, source, source_port, destination, destination_port, description):
    url = f"{PFSENSE_API_URL}firewall/rule"
    data = {
        "action": action,
        "interface": interface,
        "protocol": protocol,
        "source": {
            "network": source,
            "port": source_port
        },
        "destination": {
            "network": destination,
            "port": destination_port
        },
        "description": description
    }
    response = requests.post(url, headers=headers, json=data)
    return response.status_code == 200

def configure_nat_rule(interface, protocol, external_port, internal_ip, internal_port, description):
    url = f"{PFSENSE_API_URL}firewall/nat"
    data = {
        "interface": interface,
        "protocol": protocol,
        "external_port": external_port,
        "internal_ip": internal_ip,
        "internal_port": internal_port,
        "description": description
    }
    response = requests.post(url, headers=headers, json=data)
    return response.status_code == 200

if __name__ == "__main__":
    # Add a firewall rule to allow LAN to any
    rule_success = add_firewall_rule(
        action="pass",
        interface="lan",
        protocol="tcp",
        source="lan",
        source_port="any",
        destination="any",
        destination_port="any",
        description="Allow LAN to any"
    )
    if rule_success:
        print("Firewall rule added successfully")
    else:
        print("Failed to add firewall rule")

    # Add a NAT rule to forward HTTP traffic
    nat_success = configure_nat_rule(
        interface="wan",
        protocol="tcp",
        external_port=80,
        internal_ip="192.168.1.100",
        internal_port=80,
        description="Port forward HTTP to internal web server"
    )
    if nat_success:
        print("NAT rule added successfully")
    else:
        print("Failed to add NAT rule")

