import requests
from config import PFSENSE_API_URL, PFSENSE_API_KEY

headers = {
    'Authorization': f'Bearer {PFSENSE_API_KEY}',
    'Content-Type': 'application/json'
}

def configure_dns_resolver(dns1, dns2):
    url = f"{PFSENSE_API_URL}services/dns/resolver"
    data = {
        "dns1": dns1,
        "dns2": dns2
    }
    response = requests.post(url, headers=headers, json=data)
    return response.status_code == 200

def configure_dhcp_server(interface, start_ip, end_ip, gateway, dns_servers):
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

def configure_ddns(provider, hostname, username, password):
    url = f"{PFSENSE_API_URL}services/dynamicdns"
    data = {
        "provider": provider,
        "hostname": hostname,
        "username": username,
        "password": password
    }
    response = requests.post(url, headers=headers, json=data)
    return response.status_code == 200

if __name__ == "__main__":
    # Configure DNS Resolver
    dns_success = configure_dns_resolver("8.8.8.8", "8.8.4.4")
    if dns_success:
        print("DNS Resolver configured successfully")
    else:
        print("Failed to configure DNS Resolver")

    # Configure DHCP Server for LAN
    dhcp_success = configure_dhcp_server("lan", "192.168.1.100", "192.168.1.200", "192.168.1.1", ["8.8.8.8", "8.8.4.4"])
    if dhcp_success:
        print("DHCP Server configured successfully")
    else:
        print("Failed to configure DHCP Server")

    # Configure Dynamic DNS
    ddns_success = configure_ddns("noip", "myhostname.noip.com", "myusername", "mypassword")
    if ddns_success:
        print("Dynamic DNS configured successfully")
    else:
        print("Failed to configure Dynamic DNS")

