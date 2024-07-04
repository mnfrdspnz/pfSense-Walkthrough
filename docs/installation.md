# Installation Guide: Setting up pfSense in VirtualBox

## Introduction
This guide will walk you through the process of setting up pfSense in VirtualBox from scratch. Even if you've never used VirtualBox before, this guide will provide step-by-step instructions to get you up and running.

## Prerequisites
Before you begin, ensure you have the following:
- A computer with internet access
- Administrative privileges on your computer
- At least 2GB of free RAM
- At least 10GB of free disk space

## Step 1: Download pfSense ISO
1. Open your web browser and go to the [pfSense download page](https://www.pfsense.org/download/).
2. Select the appropriate architecture for your system (most likely `AMD64` for modern PCs).
3. Choose a mirror close to your location to download the ISO file.
4. Click the `Download` button and wait for the download to complete.

## Step 2: Install VirtualBox
1. Open your web browser and go to the [VirtualBox download page](https://www.virtualbox.org/).
2. Click on the `Download VirtualBox` button.
3. Select the installer for your operating system (Windows, macOS, Linux).
4. Download and run the installer.
5. Follow the installation prompts:
   - On Windows, click `Next`, `Next`, `Yes`, `Install`, and `Finish`.
   - On macOS, drag the VirtualBox icon to the Applications folder.
   - On Linux, use your package manager to install VirtualBox.

## Step 3: Create a New Virtual Machine in VirtualBox
1. Open VirtualBox.
2. Click on the `New` button to create a new virtual machine.
3. Name your VM (e.g., `pfSense`). VirtualBox will automatically set the Type to `BSD` and Version to `FreeBSD (64-bit)`.
4. Click `Next`.

## Step 4: Allocate Memory (RAM) for the VM
1. Use the slider to allocate memory to the VM. It is recommended to allocate at least 1024MB (1GB) of RAM.
2. Click `Next`.

## Step 5: Create a Virtual Hard Disk
1. Select `Create a virtual hard disk now` and click `Create`.
2. Choose `VDI (VirtualBox Disk Image)` and click `Next`.
3. Select `Dynamically allocated` and click `Next`.
4. Set the size of the virtual hard disk. It is recommended to allocate at least 10GB.
5. Click `Create`.

## Step 6: Configure the Virtual Machine
1. Select your newly created VM and click `Settings`.
2. Go to the `System` tab and ensure `Enable EFI` is unchecked.
3. Go to the `Storage` tab:
   - Under `Controller: IDE`, click the empty disk icon.
   - Click the disk icon next to `Optical Drive` and select `Choose a disk file`.
   - Navigate to the downloaded pfSense ISO file and select it.
4. Go to the `Network` tab:
   - Adapter 1: Attached to `Bridged Adapter` (for LAN).
   - Adapter 2: Click `Enable Network Adapter`, select `Attached to: NAT` (for WAN).

## Step 7: Start the Virtual Machine
1. Click `OK` to close the settings window.
2. Select your VM and click `Start`.
3. The VM will boot from the pfSense ISO. Follow the installation prompts:
   - Select `Install pfSense`.
   - Choose `Accept these settings`.
   - Select `Auto (UFS)` for the partitioning.
   - Wait for the installation to complete.
   - When prompted, remove the ISO from the virtual drive and reboot the VM.

## Step 8: Initial Setup
1. After the VM reboots, you will see the pfSense console menu.
2. Access the pfSense web interface:
   - Open your web browser and go to the LAN IP address (default is `http://192.168.1.1`).
   - Login with the default credentials (`admin` / `pfsense`).
3. Follow the pfSense setup wizard to complete the initial configuration.

## Next Steps
After completing the installation, you can proceed with the initial setup and further configurations as described in the other guides in this repository.

Congratulations! You have successfully installed pfSense in VirtualBox.

