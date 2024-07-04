# Basic Configuration Guide for pfSense

## Introduction
This guide will walk you through the basic configuration of your pfSense instance, including network settings, firewall configuration, and system management.

## Step 1: Network Settings

### Configuring LAN and WAN Interfaces
1. **Access the Interfaces Menu**:
   - In the pfSense web interface, go to `Interfaces > Assignments`.

2. **Configure the LAN Interface**:
   - Click on the `LAN` interface.
   - **IPv4 Configuration Type**: Select `Static IPv4`.
   - **IPv4 Address**: Enter the desired LAN IP address (e.g., `192.168.1.1/24`).
   - **IPv6 Configuration Type**: Select `None` unless you need IPv6.
   - Click `Save` and then `Apply Changes`.

3. **Configure the WAN Interface**:
   - Click on the `WAN` interface.
   - **IPv4 Configuration Type**: Select the type of connection provided by your ISP (e.g., `DHCP`, `Static IPv4`).
     - For `DHCP`: The interface will automatically receive an IP address from your ISP.
     - For `Static IPv4`: Enter the IP address, subnet mask, and gateway provided by your ISP.
   - **IPv6 Configuration Type**: Select the type of connection provided by your ISP (if applicable).
   - Click `Save` and then `Apply Changes`.

### DHCP and Static IP Setup
1. **Configure DHCP Server on LAN**:
   - Go to `Services > DHCP Server`.
   - Select the `LAN` tab.
   - Check the `Enable DHCP server on LAN interface` box.
   - **Range**: Set the range of IP addresses to be assigned by the DHCP server (e.g., `192.168.1.100` to `192.168.1.200`).
   - **DNS Servers**: Enter the IP addresses of DNS servers to be provided to clients (optional).
   - Click `Save`.

2. **Assign Static IPs to Devices**:
   - In the DHCP Server settings, scroll down to the `DHCP Static Mappings for this Interface` section.
   - Click `Add`.
   - **MAC Address**: Enter the MAC address of the device.
   - **IP Address**: Enter the desired static IP address for the device.
   - **Hostname**: Enter a hostname for the device (optional).
   - Click `Save`.

## Step 2: Firewall Configuration

### Basic Firewall Rules
1. **Access the Firewall Rules Menu**:
   - Go to `Firewall > Rules`.

2. **Add a New Rule for LAN**:
   - Select the `LAN` tab.
   - Click the `Add` button to create a new rule.
   - **Action**: Select `Pass`.
   - **Interface**: Select `LAN`.
   - **Address Family**: Select `IPv4` (or `IPv4+IPv6` if using both).
   - **Protocol**: Select `Any`.
   - **Source**: Select `LAN net`.
   - **Destination**: Select `Any`.
   - **Description**: Enter a description for the rule (e.g., `Allow LAN to Any`).
   - Click `Save` and then `Apply Changes`.

3. **Add a New Rule for WAN**:
   - Select the `WAN` tab.
   - Click the `Add` button to create a new rule.
   - **Action**: Select `Block`.
   - **Interface**: Select `WAN`.
   - **Address Family**: Select `IPv4` (or `IPv4+IPv6` if using both).
   - **Protocol**: Select `Any`.
   - **Source**: Select `Any`.
   - **Destination**: Select `Any`.
   - **Description**: Enter a description for the rule (e.g., `Block WAN to Any`).
   - Click `Save` and then `Apply Changes`.

### Port Forwarding and NAT
1. **Access the NAT Port Forward Menu**:
   - Go to `Firewall > NAT`.
   - Select the `Port Forward` tab.

2. **Create a New Port Forwarding Rule**:
   - Click the `Add` button to create a new rule.
   - **Interface**: Select `WAN`.
   - **Protocol**: Select the appropriate protocol (e.g., `TCP`).
   - **Destination Address**: Select `WAN address`.
   - **Destination Port Range**: Enter the port range to be forwarded (e.g., `80` for HTTP).
   - **Redirect Target IP**: Enter the IP address of the internal device (e.g., `192.168.1.100`).
   - **Redirect Target Port**: Enter the target port (e.g., `80`).
   - **Description**: Enter a description for the rule (e.g., `Port Forward HTTP to Web Server`).
   - Click `Save` and then `Apply Changes`.

## Step 3: System Management

### Firmware Updates
1. **Check for Firmware Updates**:
   - Go to `System > Firmware`.
   - Click the `Check for Updates` button.
   - If an update is available, follow the prompts to download and install the update.

### Backup and Restore Settings
1. **Backup Configuration**:
   - Go to `Diagnostics > Backup & Restore`.
   - Click the `Download Configuration` button to save a backup of the current configuration.

2. **Restore Configuration**:
   - Go to `Diagnostics > Backup & Restore`.
   - In the `Restore Configuration` section, click `Choose File` and select a previously saved backup file.
   - Click `Restore Configuration` to apply the backup.

## Conclusion
You have now completed the basic configuration of your pfSense instance. You can continue to explore and configure additional features such as advanced firewall rules, VPNs, VLANs, and QoS by referring to the other guides in this repository.

Congratulations! Your pfSense firewall is now set up and ready to protect your network.

