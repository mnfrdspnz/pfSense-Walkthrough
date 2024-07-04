# Security Best Practices Guide for pfSense

## Introduction
This guide outlines the best practices for securing your pfSense firewall. By following these recommendations, you can enhance the security of your network and protect it from potential threats.

## Step 1: Securing pfSense

### Change Default Admin Password
1. **Access the Web Interface**:
   - Log in to the pfSense web interface.
2. **Navigate to the Password Change Section**:
   - Go to `System > User Manager`.
   - Click on the `admin` user.
3. **Change the Password**:
   - Enter a new, strong password.
   - Confirm the new password.
   - Click `Save`.

### Configure HTTPS for the Web Interface
1. **Generate a Certificate**:
   - Go to `System > Cert Manager`.
   - Click on the `Certificates` tab.
   - Click `Add` to create a new certificate.
   - Fill in the required information and select `Create an internal certificate`.
   - Click `Save`.

2. **Enable HTTPS**:
   - Go to `System > Advanced > Admin Access`.
   - In the `WebGUI` section, select `HTTPS` for the Protocol.
   - Select the certificate you just created.
   - Click `Save`.

### Restrict Web Interface Access
1. **Change the Default Web Interface Port**:
   - Go to `System > Advanced > Admin Access`.
   - In the `WebGUI` section, change the TCP Port from `443` to a custom port (e.g., `8443`).
   - Click `Save`.

2. **Create Firewall Rules to Restrict Access**:
   - Go to `Firewall > Rules`.
   - Select the `WAN` tab.
   - Click `Add` to create a new rule.
   - Set the action to `Block` for any traffic destined to the pfSense web interface port from external networks.
   - Click `Save` and then `Apply Changes`.

### Enable SSH Access with Key-Based Authentication
1. **Generate SSH Keys**:
   - Generate SSH keys on your client machine:
     ```sh
     ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
     ```
   - Copy the public key to your clipboard:
     ```sh
     cat ~/.ssh/id_rsa.pub
     ```

2. **Configure SSH on pfSense**:
   - Go to `System > Advanced > Admin Access`.
   - Enable `Secure Shell` (SSH).
   - Paste the public key into the `Authorized Keys` box.
   - Click `Save`.

### Configure Firewall Rules
1. **Review and Harden Firewall Rules**:
   - Go to `Firewall > Rules`.
   - Review existing rules and remove any unnecessary ones.
   - Ensure default deny rules are in place for both WAN and LAN interfaces.

2. **Enable Logging for Critical Rules**:
   - Enable logging for rules that block or allow critical traffic.
   - Regularly review logs to detect any suspicious activity.

### Configure Intrusion Detection and Prevention (IDS/IPS)
1. **Install Snort or Suricata**:
   - Go to `System > Package Manager > Available Packages`.
   - Search for `Snort` or `Suricata` and click `Install`.
   - Follow the prompts to complete the installation.

2. **Configure IDS/IPS**:
   - Go to `Services > Snort` (or `Services > Suricata`).
   - Enable IDS/IPS on the desired interfaces.
   - Configure rulesets and update them regularly.
   - Enable automatic blocking of detected threats.

## Step 2: User Management

### Create and Manage User Accounts
1. **Access the User Manager**:
   - Go to `System > User Manager`.

2. **Create a New User**:
   - Click `Add` to create a new user.
   - Fill in the required information, including username and password.
   - Assign appropriate privileges to the new user.
   - Click `Save`.

3. **Manage User Privileges**:
   - Click on an existing user to modify their privileges.
   - Assign roles based on the principle of least privilege.
   - Click `Save`.

### Configure Two-Factor Authentication (2FA)
1. **Install the FreeRADIUS Package**:
   - Go to `System > Package Manager > Available Packages`.
   - Search for `FreeRADIUS` and click `Install`.
   - Follow the prompts to complete the installation.

2. **Configure FreeRADIUS**:
   - Go to `Services > FreeRADIUS`.
   - Add users and configure the authentication settings.
   - Enable 2FA by integrating with Google Authenticator or another 2FA provider.

### Monitor User Activity
1. **Enable Logging for User Actions**:
   - Go to `System > Settings > Logging`.
   - Enable logging for user login and logout events.

2. **Review Logs Regularly**:
   - Go to `Status > System Logs`.
   - Review logs to monitor user activity and detect any unauthorized access attempts.

## Step 3: Regular Maintenance and Updates

### Schedule Regular Backups
1. **Configure Automated Backups**:
   - Go to `Diagnostics > Backup & Restore`.
   - Set up automated backups to save configuration files regularly.
   - Store backups securely offsite.

### Apply Security Patches and Updates
1. **Check for Updates Regularly**:
   - Go to `System > Firmware > Updates`.
   - Check for and apply available updates and patches.

2. **Enable Automatic Updates**:
   - Go to `System > Firmware > Settings`.
   - Enable automatic updates for security patches.

### Perform Regular Security Audits
1. **Conduct Vulnerability Scans**:
   - Use tools like Nessus or OpenVAS to conduct regular vulnerability scans of your pfSense firewall.
   - Address any identified vulnerabilities promptly.

2. **Review Security Logs**:
   - Regularly review security logs for signs of suspicious activity.
   - Investigate and address any anomalies.

## Conclusion
By following these security best practices, you can significantly enhance the security of your pfSense firewall. Regular maintenance, user management, and proactive monitoring are key to maintaining a secure network environment.
