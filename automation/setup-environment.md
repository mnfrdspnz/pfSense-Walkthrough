# Setup Environment for API Integration and Automation with pfSense

## Introduction
This guide will walk you through the process of setting up the environment to interact with the pfSense API using Python. We will cover the necessary configurations on both the pfSense side and the management system side.

## Step 1: Enable API Access on pfSense

### Install and Configure pfSense API Package
1. **Access the Package Manager**:
   - In the pfSense web interface, navigate to `System > Package Manager`.

2. **Install the pfSense API Package**:
   - Go to the `Available Packages` tab.
   - Search for `pfSense-pkg-API` and click `Install`.
   - Follow the prompts to complete the installation.

3. **Enable the API**:
   - Once installed, go to `Services > API`.
   - Enable the API service and configure the settings:
     - **Access Control**: Define the allowed IP addresses or networks that can access the API.
     - **Authentication**: Use a strong username and password for API access.
     - **Permissions**: Assign appropriate permissions to the API user to ensure secure access.
   - Click `Save` to apply the settings.

### Generate API Key
1. **Generate API Key**:
   - Navigate to `Services > API > Keys`.
   - Click `Add` to generate a new API key.
   - Provide a description for the key and select the user account.
   - Copy and save the generated API key securely.

## Step 2: Set Up the Management System

### Install Python and Necessary Libraries
1. **Install Python**:
   - Ensure Python is installed on your management system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Set Up a Virtual Environment**:
   - Create and activate a virtual environment to manage dependencies:
     ```bash
     python3 -m venv pfsense-automation-env
     source pfsense-automation-env/bin/activate
     ```

3. **Install Required Python Libraries**:
   - Install the necessary libraries for API interaction and automation:
     ```bash
     pip install requests
     ```

### Create a Configuration File
1. **Create a Configuration File**:
   - Create a file named `config.py` to store the API URL, username, and API key:
     ```python
     # config.py

     PFSENSE_API_URL = "https://your-pfsense-ip-address/api/v1/"
     PFSENSE_API_KEY = "your-api-key"
     ```

## Step 3: Test API Connectivity

### Write a Simple Python Script to Test Connectivity
1. **Create a Test Script**:
   - Create a file named `test_api.py` and add the following content:
     ```python
     import requests
     from config import PFSENSE_API_URL, PFSENSE_API_KEY

     headers = {
         'Authorization': f'Bearer {PFSENSE_API_KEY}',
         'Content-Type': 'application/json'
     }

     def get_system_info():
         url = f"{PFSENSE_API_URL}system/status"
         response = requests.get(url, headers=headers)
         if response.status_code == 200:
             return response.json()
         else:
             return None

     if __name__ == "__main__":
         system_info = get_system_info()
         if system_info:
             print("System Info:", system_info)
         else:
             print("Failed to connect to pfSense API")
     ```

2. **Run the Test Script**:
   - Execute the test script to verify API connectivity:
     ```bash
     python test_api.py
     ```
   - If the connection is successful, you should see the system information printed in the console.

## Step 4: Automate Common Tasks

### Create Python Scripts for Automation

1. **Network Configuration Script**:
   - Create a file named `network_configuration.py` and add the following content:
     ```python
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

     if __name__ == "__main__":
         success = configure_interface("lan", "192.168.1.1", "24")
         if success:
             print("Interface configured successfully")
         else:
             print("Failed to configure interface")
     ```

2. **Firewall Configuration Script**:
   - Create a file named `firewall_configuration.py` and add the following content:
     ```python
     import requests
     from config import PFSENSE_API_URL, PFSENSE_API_KEY

     headers = {
         'Authorization': f'Bearer {PFSENSE_API_KEY}',
         'Content-Type': 'application/json'
     }

     def add_firewall_rule(action, interface, protocol, source, destination, description):
         url = f"{PFSENSE_API_URL}firewall/rule"
         data = {
             "action": action,
             "interface": interface,
             "protocol": protocol,
             "source": source,
             "destination": destination,
             "description": description
         }
         response = requests.post(url, headers=headers, json=data)
         return response.status_code == 200

     if __name__ == "__main__":
         success = add_firewall_rule("pass", "lan", "tcp", "192.168.1.0/24", "any", "Allow LAN to Any")
         if success:
             print("Firewall rule added successfully")
         else:
             print("Failed to add firewall rule")
     ```

## Conclusion
By following this guide, you have set up the environment to interact with the pfSense API using Python. You can now create and run Python scripts to automate various aspects of pfSense management.

Congratulations! Your environment is now configured for API integration and automation with pfSense.
