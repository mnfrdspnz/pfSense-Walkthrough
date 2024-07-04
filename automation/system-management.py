import requests
from config import PFSENSE_API_URL, PFSENSE_API_KEY

headers = {
    'Authorization': f'Bearer {PFSENSE_API_KEY}',
    'Content-Type': 'application/json'
}

def update_firmware():
    url = f"{PFSENSE_API_URL}system/firmware/update"
    response = requests.post(url, headers=headers)
    return response.status_code == 200

def backup_configuration():
    url = f"{PFSENSE_API_URL}system/config/backup"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open('config-backup.xml', 'wb') as f:
            f.write(response.content)
        return True
    else:
        return False

def restore_configuration(backup_file_path):
    url = f"{PFSENSE_API_URL}system/config/restore"
    with open(backup_file_path, 'rb') as f:
        files = {'config.xml': f}
        response = requests.post(url, headers=headers, files=files)
    return response.status_code == 200

if __name__ == "__main__":
    # Update firmware
    update_success = update_firmware()
    if update_success:
        print("Firmware update initiated successfully")
    else:
        print("Failed to initiate firmware update")

    # Backup configuration
    backup_success = backup_configuration()
    if backup_success:
        print("Configuration backup successful")
    else:
        print("Failed to backup configuration")

    # Restore configuration from a backup file
    # Ensure 'config-backup.xml' is available in the same directory
    restore_success = restore_configuration('config-backup.xml')
    if restore_success:
        print("Configuration restored successfully")
    else:
        print("Failed to restore configuration")

