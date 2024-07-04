# Initial Setup Guide for pfSense

## Introduction
This guide will walk you through the initial setup of your pfSense instance after installation. We'll cover accessing the web interface, setting up the basic configuration, and getting your network up and running.

## Step 1: Access the pfSense Web Interface
1. **Determine the LAN IP Address**:
   - After installation, the pfSense console will display the LAN IP address. The default LAN IP address is `192.168.1.1`.

2. **Connect to the Web Interface**:
   - Open a web browser on a computer connected to the LAN network.
   - Type the LAN IP address into the browser's address bar (e.g., `http://192.168.1.1`).
   - You will see a security warning. This is because pfSense uses a self-signed SSL certificate. Proceed by clicking `Advanced` and then `Proceed to 192.168.1.1 (unsafe)`.

3. **Login to the Web Interface**:
   - Enter the default username: `admin`
   - Enter the default password: `pfsense`
   - Click `Sign In`.

## Step 2: Run the Setup Wizard
1. **Welcome Screen**:
   - The pfSense setup wizard will start. Click `Next` to proceed.

2. **Set the Hostname, Domain, and DNS Servers**:
   - **Hostname**: Enter a name for your pfSense device (e.g., `pfSenseRouter`).
   - **Domain**: Enter your network domain (e.g., `localdomain`).
   - **Primary DNS Server**: Enter the IP address of your primary DNS server (e.g., `8.8.8.8` for Google DNS).
   - **Secondary DNS Server**: Enter the IP address of your secondary DNS server (optional, e.g., `8.8.4.4` for Google DNS).
   - Click `Next`.

3. **Configure the Time Server and Time Zone**:
   - **NTP Server**: Use the default (pool.ntp.org).
   - **Time Zone**: Select your time zone from the dropdown menu.
   - Click `Next`.

4. **Configure the WAN Interface**:
   - **Type**: Select the type of WAN connection (e.g., DHCP, Static).
     - For DHCP: Select `DHCP`.
     - For Static IP: Select `Static` and enter the required information (IP address, subnet mask, gateway).
   - **MTU**: Leave at default unless instructed by your ISP.
   - **MSS**: Leave at default unless instructed by your ISP.
   - **Enable/Disable DHCP6**: Select according to your ISP's instructions.
   - Click `Next`.

5. **Configure the LAN Interface**:
   - **IP Address**: Set the IP address for the LAN interface (default is `192.168.1.1`).
   - **Subnet Mask**: Set the subnet mask for the LAN network (default is `24` for `255.255.255.0`).
   - Click `Next`.

6. **Set the Admin Password**:
   - Enter a new password for the `admin` account.
   - Confirm the password.
   - Click `Next`.

7. **Reload Configuration**:
   - The setup wizard will display a summary of your settings. Click `Reload` to apply the changes.

## Step 3: Finalize the Configuration
1. **Reboot the pfSense Device**:
   - After the setup wizard completes, it is a good idea to reboot your pfSense device to ensure all settings are properly applied.
   - Go to `Diagnostics > Reboot` in the web interface.
   - Click `Reboot`.

2. **Verify Connectivity**:
   - Ensure your devices connected to the LAN network can access the internet.
   - Test accessing various websites to confirm that DNS and routing are working correctly.

## Next Steps
With the basic setup complete, you can proceed to configure additional features such as:
- Advanced firewall rules
- VPN setup
- VLANs and subnetting
- Quality of Service (QoS)

Refer to the other guides in this repository for detailed instructions on these topics.

Congratulations! You have successfully completed the initial setup of your pfSense device.

