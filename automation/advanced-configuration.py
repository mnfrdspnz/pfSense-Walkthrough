import requests
from config import PFSENSE_API_URL, PFSENSE_API_KEY

headers = {
    'Authorization': f'Bearer {PFSENSE_API_KEY}',
    'Content-Type': 'application/json'
}

def configure_vlan(interface, vlan_tag, vlan_description):
    url = f"{PFSENSE_API_URL}interface/vlan"
    data = {
        "parent": interface,
        "tag": vlan_tag,
        "description": vlan_description
    }
    response = requests.post(url, headers=headers, json=data)
    return response.status_code == 200

def configure_qos(interface, queue, priority):
    url = f"{PFSENSE_API_URL}qos/queue"
    data = {
        "interface": interface,
        "queue": queue,
        "priority": priority
    }
    response = requests.post(url, headers=headers, json=data)
    return response.status_code == 200

def configure_openvpn_server(server_data):
    url = f"{PFSENSE_API_URL}vpn/openvpn/server"
    response = requests.post(url, headers=headers, json=server_data)
    return response.status_code == 200

def configure_wireguard_vpn(vpn_data):
    url = f"{PFSENSE_API_URL}vpn/wireguard"
    response = requests.post(url, headers=headers, json=vpn_data)
    return response.status_code == 200

if __name__ == "__main__":
    # Configure VLAN
    vlan_success = configure_vlan("em0", 10, "Management VLAN")
    if vlan_success:
        print("VLAN configured successfully")
    else:
        print("Failed to configure VLAN")

    # Configure QoS
    qos_success = configure_qos("lan", "high_priority", 7)
    if qos_success:
        print("QoS configured successfully")
    else:
        print("Failed to configure QoS")

    # Configure OpenVPN Server
    openvpn_server_data = {
        "description": "Remote Access VPN",
        "servermode": "remote_access",
        "protocol": "udp",
        "device_mode": "tun",
        "interface": "wan",
        "local_port": 1194,
        "crypto": "AES-256-CBC",
        "authmode": "Local Database",
        "tunnel_network": "10.8.0.0/24",
        "local_network": "192.168.1.0/24",
        "compression": "lz4",
        "dns_domain": "localdomain",
        "dns_server1": "8.8.8.8",
        "dns_server2": "8.8.4.4"
    }
    openvpn_success = configure_openvpn_server(openvpn_server_data)
    if openvpn_success:
        print("OpenVPN server configured successfully")
    else:
        print("Failed to configure OpenVPN server")

    # Configure WireGuard VPN
    wireguard_vpn_data = {
        "interface": "wg0",
        "address": "10.10.10.1/24",
        "port": 51820,
        "peers": [
            {
                "public_key": "peer_public_key",
                "allowed_ips": "10.10.10.2/32",
                "endpoint": "peer_endpoint:51820"
            }
        ]
    }
    wireguard_success = configure_wireguard_vpn(wireguard_vpn_data)
    if wireguard_success:
        print("WireGuard VPN configured successfully")
    else:
        print("Failed to configure WireGuard VPN")

