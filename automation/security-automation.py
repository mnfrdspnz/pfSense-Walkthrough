import requests
from config import PFSENSE_API_URL, PFSENSE_API_KEY

headers = {
    'Authorization': f'Bearer {PFSENSE_API_KEY}',
    'Content-Type': 'application/json'
}

def create_user(username, password, privileges):
    url = f"{PFSENSE_API_URL}user"
    data = {
        "username": username,
        "password": password,
        "privileges": privileges
    }
    response = requests.post(url, headers=headers, json=data)
    return response.status_code == 200

def set_firewall_rule_logging(rule_id, logging):
    url = f"{PFSENSE_API_URL}firewall/rule/{rule_id}"
    data = {
        "logging": logging
    }
    response = requests.put(url, headers=headers, json=data)
    return response.status_code == 200

def enable_ssh_key_auth(username, ssh_key):
    url = f"{PFSENSE_API_URL}system/ssh/key"
    data = {
        "username": username,
        "ssh_key": ssh_key
    }
    response = requests.post(url, headers=headers, json=data)
    return response.status_code == 200

def configure_2fa(username, secret):
    url = f"{PFSENSE_API_URL}user/2fa"
    data = {
        "username": username,
        "secret": secret
    }
    response = requests.post(url, headers=headers, json=data)
    return response.status_code == 200

if __name__ == "__main__":
    # Create a new user with admin privileges
    user_success = create_user("newadmin", "securepassword", ["ALL"])
    if user_success:
        print("User created successfully")
    else:
        print("Failed to create user")

    # Enable logging for a specific firewall rule
    logging_success = set_firewall_rule_logging(1, True)
    if logging_success:
        print("Logging enabled for firewall rule")
    else:
        print("Failed to enable logging for firewall rule")

    # Enable SSH key authentication for a user
    ssh_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQD..."
    ssh_success = enable_ssh_key_auth("newadmin", ssh_key)
    if ssh_success:
        print("SSH key authentication enabled")
    else:
        print("Failed to enable SSH key authentication")

    # Configure 2FA for a user
    secret = "JBSWY3DPEHPK3PXP"
    twofa_success = configure_2fa("newadmin", secret)
    if twofa_success:
        print("2FA configured successfully")
    else:
        print("Failed to configure 2FA")

