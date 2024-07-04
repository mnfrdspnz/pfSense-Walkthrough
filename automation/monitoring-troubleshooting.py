import requests
from config import PFSENSE_API_URL, PFSENSE_API_KEY

headers = {
    'Authorization': f'Bearer {PFSENSE_API_KEY}',
    'Content-Type': 'application/json'
}

def get_system_status():
    url = f"{PFSENSE_API_URL}system/status"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_interface_status(interface):
    url = f"{PFSENSE_API_URL}interface/{interface}/status"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_firewall_logs():
    url = f"{PFSENSE_API_URL}logs/firewall"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def perform_ping_test(host):
    url = f"{PFSENSE_API_URL}diagnostics/ping"
    data = {
        "host": host,
        "count": 4
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == "__main__":
    # Get system status
    system_status = get_system_status()
    if system_status:
        print("System Status:", system_status)
    else:
        print("Failed to retrieve system status")

    # Get interface status for LAN
    interface_status = get_interface_status("lan")
    if interface_status:
        print("LAN Interface Status:", interface_status)
    else:
        print("Failed to retrieve LAN interface status")

    # Get firewall logs
    firewall_logs = get_firewall_logs()
    if firewall_logs:
        print("Firewall Logs:", firewall_logs)
    else:
        print("Failed to retrieve firewall logs")

    # Perform a ping test
    ping_result = perform_ping_test("8.8.8.8")
    if ping_result:
        print("Ping Test Result:", ping_result)
    else:
        print("Failed to perform ping test")

