# Packages and Extensions Guide for pfSense

## Introduction
This guide covers how to manage packages and extensions in pfSense. You'll learn how to install and remove packages, as well as explore commonly used packages that can enhance the functionality of your pfSense firewall.

## Step 1: Package Management

### Installing Packages
1. **Access the Package Manager**:
   - In the pfSense web interface, navigate to `System > Package Manager`.

2. **Browse Available Packages**:
   - Click on the `Available Packages` tab.
   - You will see a list of available packages that can be installed.

3. **Install a Package**:
   - Find the package you want to install (e.g., `OpenVPN`, `pfBlockerNG`).
   - Click the `Install` button next to the package.
   - Confirm the installation by clicking `Confirm`.
   - Wait for the installation to complete. You will see a message indicating that the package has been installed successfully.

### Removing Packages
1. **Access the Package Manager**:
   - Navigate to `System > Package Manager`.

2. **View Installed Packages**:
   - Click on the `Installed Packages` tab.
   - You will see a list of packages that are currently installed.

3. **Remove a Package**:
   - Find the package you want to remove.
   - Click the `Remove` button next to the package.
   - Confirm the removal by clicking `Confirm`.
   - Wait for the removal process to complete. You will see a message indicating that the package has been removed successfully.

## Step 2: Commonly Used Packages

### OpenVPN
1. **Purpose**: Provides VPN functionality to create secure connections.
2. **Installation**:
   - Go to `System > Package Manager > Available Packages`.
   - Search for `OpenVPN` and click `Install`.
   - Follow the prompts to complete the installation.

### pfBlockerNG
1. **Purpose**: Enhances the firewall by blocking advertisements, tracking, and malicious sites.
2. **Installation**:
   - Go to `System > Package Manager > Available Packages`.
   - Search for `pfBlockerNG` and click `Install`.
   - Follow the prompts to complete the installation.

### Snort
1. **Purpose**: Provides network intrusion detection and prevention capabilities.
2. **Installation**:
   - Go to `System > Package Manager > Available Packages`.
   - Search for `Snort` and click `Install`.
   - Follow the prompts to complete the installation.

### Squid
1. **Purpose**: Implements a caching proxy server to improve web performance and security.
2. **Installation**:
   - Go to `System > Package Manager > Available Packages`.
   - Search for `Squid` and click `Install`.
   - Follow the prompts to complete the installation.

### Suricata
1. **Purpose**: Provides real-time intrusion detection and prevention.
2. **Installation**:
   - Go to `System > Package Manager > Available Packages`.
   - Search for `Suricata` and click `Install`.
   - Follow the prompts to complete the installation.

## Step 3: Custom Scripts

### Writing and Deploying Custom Scripts
1. **Access the Shell**:
   - In the pfSense web interface, go to `Diagnostics > Command Prompt`.
   - Alternatively, you can access the shell via SSH if it is enabled.

2. **Create a Script**:
   - Use the shell to create a new script file. For example, to create a script that pings a specific IP address, you can use the following command:
     ```sh
     echo '#!/bin/sh' > /root/ping-script.sh
     echo 'ping -c 4 8.8.8.8' >> /root/ping-script.sh
     chmod +x /root/ping-script.sh
     ```

3. **Execute the Script**:
   - Run the script from the shell to verify it works:
     ```sh
     /root/ping-script.sh
     ```

### Automation Tasks Using Scripts
1. **Automating Backups**:
   - Create a script to automate the backup process:
     ```sh
     echo '#!/bin/sh' > /root/backup-script.sh
     echo 'cp /cf/conf/config.xml /root/config-$(date +%F).xml' >> /root/backup-script.sh
     chmod +x /root/backup-script.sh
     ```
   - Schedule the script to run at a specific time using Cron:
     - Go to `Services > Cron`.
     - Add a new Cron job to run the script at the desired time.

2. **Automating Updates**:
   - Create a script to automate the update process:
     ```sh
     echo '#!/bin/sh' > /root/update-script.sh
     echo 'pfSense-upgrade' >> /root/update-script.sh
     chmod +x /root/update-script.sh
     ```
   - Schedule the script to run at a specific time using Cron:
     - Go to `Services > Cron`.
     - Add a new Cron job to run the script at the desired time.

## Conclusion
By managing packages and deploying custom scripts, you can extend the functionality of your pfSense firewall and automate routine tasks. These enhancements will help you optimize and secure your network more effectively.
