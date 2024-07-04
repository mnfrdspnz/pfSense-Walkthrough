# Monitoring and Troubleshooting Guide for pfSense

## Introduction
This guide provides detailed instructions on how to monitor and troubleshoot your pfSense firewall. It covers various tools and techniques to diagnose and resolve issues effectively.

## Step 1: Network Monitoring Tools

### Using the Web Interface for Monitoring

1. **Dashboard Overview**:
   - The pfSense dashboard provides a quick overview of your system's status, including CPU usage, memory usage, and interface statistics.
   - To access the dashboard, log in to the pfSense web interface. You can customize the dashboard to display the widgets you find most useful.

2. **Monitoring Interfaces**:
   - Go to `Status > Interfaces` to view detailed information about each network interface, including IP addresses, packet statistics, and error counts.
   - Check for any anomalies, such as high error rates or unusual traffic patterns.

3. **Real-Time Traffic Graphs**:
   - Navigate to `Status > Traffic Graph` to view real-time traffic graphs for each interface.
   - This helps you visualize traffic patterns and identify any unexpected spikes in traffic.

4. **Quality of Service (QoS) Monitoring**:
   - If you have configured traffic shaping, go to `Status > Queues` to monitor the performance of your QoS settings.
   - Ensure that critical traffic is being prioritized correctly.

### CLI Monitoring Tools

1. **Accessing the CLI**:
   - You can access the pfSense CLI via SSH or directly from the console.
   - To enable SSH, go to `System > Advanced > Admin Access` and enable `Secure Shell`.

2. **Using `top` for System Monitoring**:
   - Run the `top` command to display real-time system performance metrics, including CPU usage, memory usage, and running processes.
   - Look for any processes consuming excessive resources.

3. **Using `iftop` for Traffic Monitoring**:
   - Install `iftop` using the pfSense package manager:
     ```sh
     pkg install iftop
     ```
   - Run `iftop` to monitor real-time network traffic on a specific interface:
     ```sh
     iftop -i em0
     ```
   - Look for any unusual traffic patterns or high bandwidth usage.

4. **Using `vnstat` for Network Traffic Statistics**:
   - Install `vnstat` using the pfSense package manager:
     ```sh
     pkg install vnstat
     ```
   - Run `vnstat` to view network traffic statistics over different time periods:
     ```sh
     vnstat -i em0
     ```
   - Analyze historical traffic data to identify trends and anomalies.

## Step 2: Logs and Diagnostics

### Accessing System Logs

1. **View System Logs via the Web Interface**:
   - Navigate to `Status > System Logs` to view various system logs, including firewall logs, DHCP logs, and VPN logs.
   - Use the different tabs to filter logs by category.

2. **Download Logs for Analysis**:
   - You can download log files for offline analysis. Go to `Diagnostics > Command Prompt` and use the `cat` or `tail` commands to view logs.
   - Example command to download the firewall log:
     ```sh
     cat /var/log/filter.log > /tmp/firewall.log
     ```

### Common Troubleshooting Commands and Techniques

1. **Check Network Connectivity**:
   - Use the `ping` command to test connectivity to other devices:
     ```sh
     ping 8.8.8.8
     ping <LAN_IP>
     ```
   - Use `traceroute` to diagnose routing issues:
     ```sh
     traceroute 8.8.8.8
     ```

2. **Analyze Firewall Rules**:
   - Use the `pfctl` command to view the current firewall rules:
     ```sh
     pfctl -sr
     ```
   - Check for any rules that might be blocking legitimate traffic.

3. **Check Interface Status**:
   - Use the `ifconfig` command to view the status of network interfaces:
     ```sh
     ifconfig em0
     ```
   - Look for interfaces that are down or have incorrect IP configurations.

4. **Monitor Open Connections**:
   - Use the `netstat` command to view open connections and listening ports:
     ```sh
     netstat -an
     ```
   - Identify any unexpected connections that might indicate a security issue.

5. **Inspect Packet Captures**:
   - Use the `tcpdump` command to capture and analyze network traffic:
     ```sh
     tcpdump -i em0 -w /tmp/capture.pcap
     ```
   - Download the capture file and analyze it using a tool like Wireshark.

6. **Check System Performance**:
   - Use the `vmstat` command to monitor system performance metrics:
     ```sh
     vmstat 1
     ```
   - Look for high CPU or memory usage that might indicate a problem.

## Step 3: Advanced Diagnostics

### Using pfSense Diagnostic Tools

1. **Diagnostics > Ping**:
   - Use the `Ping` tool in the web interface to test connectivity to remote hosts.
   - Enter the hostname or IP address and click `Ping`.

2. **Diagnostics > Traceroute**:
   - Use the `Traceroute` tool to diagnose routing issues.
   - Enter the hostname or IP address and click `Traceroute`.

3. **Diagnostics > Packet Capture**:
   - Use the `Packet Capture` tool to capture network traffic on specific interfaces.
   - Specify the interface, packet count, and filters, then click `Start` to begin the capture.

### Checking System Health

1. **System > Advanced > Miscellaneous**:
   - Enable the `PowerD` daemon to manage power consumption and optimize performance.
   - Monitor system temperatures and hardware health.

2. **System > Advanced > Notifications**:
   - Configure email notifications to receive alerts about system issues.
   - Set up monitoring for key metrics and receive notifications when thresholds are exceeded.

## Step 4: Common Issues and Solutions

### Internet Connectivity Issues
- **Problem**: No internet access from LAN devices.
  - **Solution**: Check the WAN interface status and ensure it has a valid IP address. Verify that the default gateway and DNS settings are correct.

### Slow Network Performance
- **Problem**: Network performance is slow or intermittent.
  - **Solution**: Use traffic monitoring tools to identify bandwidth hogs. Check for interface errors and collisions. Adjust QoS settings to prioritize critical traffic.

### VPN Connectivity Issues
- **Problem**: VPN clients cannot connect to the VPN server.
  - **Solution**: Verify the VPN configuration and ensure that firewall rules allow VPN traffic. Check the status of the VPN service and logs for any errors.

### DHCP Issues
- **Problem**: Devices are not receiving IP addresses from the DHCP server.
  - **Solution**: Check the DHCP server configuration and ensure it is enabled on the correct interface. Verify that there are no IP conflicts and the DHCP range is correctly defined.

### Firewall Rule Issues
- **Problem**: Legitimate traffic is being blocked by the firewall.
  - **Solution**: Review the firewall rules and adjust them as needed. Use the `pfctl` command to view active rules and ensure they are applied correctly.

## Conclusion
By using the monitoring tools and troubleshooting techniques outlined in this guide, you can effectively diagnose and resolve issues with your pfSense firewall. Regular monitoring and proactive maintenance will help ensure the security and performance of your network.
