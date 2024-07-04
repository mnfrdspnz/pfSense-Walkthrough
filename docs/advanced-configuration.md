# Advanced Configuration Guide for pfSense

## Introduction
This guide covers advanced configurations for pfSense, including VLANs and subnetting, QoS, VPN setup, and advanced network services. It assumes you have a high level of understanding of networking concepts and are comfortable with advanced configurations.

## Step 1: VLANs and Subnetting

### Configuring VLANs
1. **Access the Interfaces Menu**:
   - Navigate to `Interfaces > Assignments`.
   - Click on the `VLANs` tab.

2. **Add a New VLAN**:
   - Click `Add`.
   - **Parent Interface**: Select the physical interface to which the VLAN will be attached (e.g., `em0`).
   - **VLAN Tag**: Enter the VLAN ID (e.g., `10`).
   - **Description**: Enter a description for the VLAN (e.g., `VLAN 10 - Management`).
   - Click `Save`.

3. **Assign the VLAN to an Interface**:
   - Go to `Interfaces > Assignments`.
   - In the `Available network ports` dropdown, select the newly created VLAN (e.g., `VLAN 10 on em0`).
   - Click `Add`.
   - Click on the new interface (e.g., `OPT1`), rename it to something meaningful (e.g., `VLAN10`), and configure it as needed (e.g., static IP, DHCP).
   - Click `Save` and then `Apply Changes`.

### Setting Up Multiple Subnets
1. **Create Subnets**:
   - Ensure you have different subnets defined for each VLAN (e.g., `192.168.10.0/24` for VLAN 10).

2. **Assign IP Addresses to VLAN Interfaces**:
   - Go to `Interfaces` and select the VLAN interface (e.g., `VLAN10`).
   - Set the IPv4 Configuration Type to `Static IPv4`.
   - Enter the IP address and subnet mask (e.g., `192.168.10.1/24`).
   - Click `Save` and then `Apply Changes`.

3. **Configure DHCP for Each Subnet**:
   - Go to `Services > DHCP Server`.
   - Select the VLAN interface tab (e.g., `VLAN10`).
   - Check the `Enable DHCP server` box.
   - Set the DHCP range (e.g., `192.168.10.100` to `192.168.10.200`).
   - Click `Save`.

## Step 2: Quality of Service (QoS)

### Traffic Shaping and Prioritization
1. **Enable Traffic Shaper**:
   - Go to `Firewall > Traffic Shaper`.
   - Click on the `Wizards` tab.
   - Select the appropriate wizard based on your needs (e.g., `Dedicated Links`, `Multiple Lan/Wan`).

2. **Configure Traffic Shaping Rules**:
   - Follow the wizard to configure the traffic shaping rules.
   - Define queues and assign priorities based on your network requirements (e.g., prioritize VoIP traffic).

3. **Apply Changes and Monitor**:
   - Apply the changes.
   - Go to `Status > Queues` to monitor the traffic shaping performance and make adjustments as needed.

### Configuring SQM (Smart Queue Management)
1. **Install the SQM Package**:
   - Go to `System > Package Manager > Available Packages`.
   - Search for and install the `SQM` package.

2. **Configure SQM**:
   - Go to `Services > Smart Queue Management`.
   - Enable SQM on the desired interface (e.g., `WAN`).
   - Configure the download and upload speeds based on your ISP plan.
   - Apply and save the changes.

## Step 3: VPN Setup

### Setting Up OpenVPN Server/Client
1. **Install the OpenVPN Package**:
   - Go to `System > Package Manager > Available Packages`.
   - Search for and install the `OpenVPN` package.

2. **Configure OpenVPN Server**:
   - Go to `VPN > OpenVPN > Wizards`.
   - Follow the wizard to set up the OpenVPN server:
     - **Type of Server**: Select `Local User Access`.
     - **Authentication Backend**: Select `Local Database`.
     - **Certificates**: Generate or select existing certificates.
     - **Tunnel Network**: Define the network for VPN clients (e.g., `10.8.0.0/24`).
     - **Local Network**: Define the local network to be accessed by VPN clients (e.g., `192.168.1.0/24`).
     - **DNS**: Provide DNS settings for the clients.

3. **Configure OpenVPN Client**:
   - Export the client configuration file from `VPN > OpenVPN > Client Export`.
   - Import the configuration file into your OpenVPN client application on your device.

### Configuring IPsec VPN
1. **Access the IPsec Configuration**:
   - Go to `VPN > IPsec`.

2. **Add a Phase 1 Entry**:
   - Click `Add` to create a new Phase 1 entry.
   - **Key Exchange Version**: Select `Auto`.
   - **Interface**: Select `WAN`.
   - **Remote Gateway**: Enter the remote IP address or hostname.
   - **Authentication Method**: Select `Mutual PSK`.
   - **Pre-Shared Key**: Enter the shared key.
   - **Phase 1 Proposal (Algorithms)**: Select the desired encryption and authentication algorithms.
   - Click `Save` and then `Apply Changes`.

3. **Add a Phase 2 Entry**:
   - Click `Show Phase 2 Entries` under the Phase 1 entry.
   - Click `Add` to create a new Phase 2 entry.
   - **Mode**: Select `Tunnel IPv4`.
   - **Local Network**: Define the local network (e.g., `192.168.1.0/24`).
   - **Remote Network**: Define the remote network (e.g., `192.168.2.0/24`).
   - **Phase 2 Proposal (Algorithms)**: Select the desired encryption and authentication algorithms.
   - Click `Save` and then `Apply Changes`.

## Step 4: Network Services

### Configuring DNS and DHCP Options
1. **Access DNS Resolver Settings**:
   - Go to `Services > DNS Resolver`.
   - Ensure the DNS Resolver is enabled.
   - Configure the DNS Resolver settings as needed (e.g., forwarder mode, DNSSEC).

2. **Configure DHCP Server Options**:
   - Go to `Services > DHCP Server`.
   - Select the desired interface tab (e.g., `LAN` or `VLAN10`).
   - Configure additional DHCP options such as DNS servers, gateway, and lease time.

### Setting Up Dynamic DNS (DDNS)
1. **Install the Dynamic DNS Package**:
   - Go to `System > Package Manager > Available Packages`.
   - Search for and install the `Dynamic DNS` package.

2. **Configure Dynamic DNS**:
   - Go to `Services > Dynamic DNS`.
   - Click `Add` to create a new DDNS entry.
   - **Service Type**: Select the DDNS provider (e.g., `DynDNS`, `No-IP`).
   - **Interface to Monitor**: Select the WAN interface.
   - **Hostname**: Enter the DDNS hostname.
   - **Username**: Enter the username for the DDNS service.
   - **Password**: Enter the password for the DDNS service.
   - Click `Save` and then `Apply Changes`.

## Conclusion
You have now completed advanced configurations for your pfSense instance. This includes setting up VLANs, configuring QoS, establishing VPN connections, and managing advanced network services. These configurations will help you manage and optimize your network effectively.

