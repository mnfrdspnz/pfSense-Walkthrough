import requests
from config import PFSENSE_API_URL, PFSENSE_API_KEY

headers = {
    'Authorization': f'Bearer {PFSENSE_API_KEY}',
    'Content-Type': 'application/json'
}

def configure_interface(interface, ip_address, subnet_mask):
    url = f"{PFSENSE_API_URL}interface/configure"
    data = {
        "interface": interface,
        "ipaddress": ip_address,
        "subnetmask": subnet_mask
    }
    response = requests.post(url, headers=headers, json=data)
    return response.status_code == 200

def configure_dhcp(interface, start_ip, end_ip, gateway, dns_servers):
    url = f"{PFSENSE_API_URL}services/dhcpd"
    data = {
        "interface": interface,
        "range": {
            "from": start_ip,
            "to": end_ip
        },
        "gateway": gateway,
        "dns_servers": dns_servers
    }
    response = requests.post(url, headers=headers, json=data)
    return response.status_code == 200

def configure_static_ip(mac_address, ip_address, interface):
    url = f"{PFSENSE_API_URL}services/dhcpd/static"
    data = {
        "mac_address": mac_address,
        "ipaddress": ip_address,
        "interface": interface
    }
    response = requests.post(url, headers=headers, json=data)
    return response.status_code == 200

if __name__ == "__main__":
    # Configure LAN interface
    lan_success = configure_interface("lan", "192.168.1.1", "24")
    if lan_success:
        print("LAN interface configured successfully")
    else:
        print("Failed to configure LAN interface")

    # Configure DHCP for LAN
    dhcp_success = configure_dhcp("lan", "192.168.1.100", "192.168.1.200", "192.168.1.1", ["8.8.8.8", "8.8.4.4"])
    if dhcp_success:
        print("DHCP configured successfully")
    else:
        print("Failed to configure DHCP")

    # Configure a static IP for a specific device
    static_ip_success = configure_static_ip("00:11:22:33:44:55", "192.168.1.50", "lan")
    if static_ip_success:
        print("Static IP configured successfully")
    else:
        print("Failed to configure static IP")

