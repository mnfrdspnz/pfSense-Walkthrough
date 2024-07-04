# Installation Guide: Setting up pfSense in VirtualBox

## Download pfSense ISO
- Go to the [pfSense download page](https://www.pfsense.org/download/).
- Select the appropriate architecture and download the ISO installer.

## Install VirtualBox
- Download and install VirtualBox from [VirtualBox.org](https://www.virtualbox.org/).

## Create a New Virtual Machine
1. Open VirtualBox and click "New".
2. Name the VM (e.g., `pfSense`), set the type to `BSD`, and version to `FreeBSD (64-bit)`.
3. Allocate memory (e.g., 1024MB).
4. Create a virtual hard disk (e.g., 10GB, VDI, dynamically allocated).

## Configure the Virtual Machine
1. Go to the settings of the newly created VM.
2. **System**: Ensure "Enable EFI" is unchecked.
3. **Storage**: Mount the pfSense ISO to the optical drive.
4. **Network**:
   - Adapter 1: Attached to `Bridged Adapter` (for LAN).
   - Adapter 2: Attached to `NAT` (for WAN).

## Start the Virtual Machine
1. Click "Start" to boot from the pfSense ISO.
2. Follow the installation prompts to install pfSense on the virtual hard disk.

## Initial Setup
1. After installation, remove the ISO from the virtual drive.
2. Reboot the VM.
3. Access the pfSense web interface using the LAN IP (default is 192.168.1.1).

