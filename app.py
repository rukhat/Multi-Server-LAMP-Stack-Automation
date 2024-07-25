import subprocess
import os
import sys
import psutil
import logging
from datetime import datetime

import app_config

db_ip = app_config.DB_IP
auth_ip = app_config.AUTH_IP
backup_scripts_dir = app_config.BACKUP_SCRIPTS_DIR
backup_storage_dir = app_config.BACKUP_STORAGE_DIR

# Configure logging
logging.basicConfig(filename='/home/vagrant/app_management.log', level=logging.INFO, format='%(asctime)s %(message)s')

# Base directory where the backup scripts will be saved
backup_scripts_dir = '/home/vagrant/backup_scripts'
backup_storage_dir = '/home/vagrant/backups'

# Function to create backup scripts if they don't exist
def create_backup_scripts():
    os.makedirs(backup_scripts_dir, exist_ok=True)
    os.makedirs(backup_storage_dir, exist_ok=True)
    logging.info(f"Created directories: {backup_scripts_dir} and {backup_storage_dir}")

    db_backup_script = os.path.join(backup_scripts_dir, 'backup_db.sh')
    auth_backup_script = os.path.join(backup_scripts_dir, 'backup_auth.sh')
    logging.info(f"DB script path: {db_backup_script}")
    logging.info(f"Auth script path: {auth_backup_script}")

    db_backup_content = f"""#!/bin/bash
rsync -avz --delete vagrant@192.168.56.10:/path/to/backup/ {backup_storage_dir}/db/
"""

    auth_backup_content = f"""#!/bin/bash
rsync -avz --delete vagrant@192.168.56.11:/path/to/backup/ {backup_storage_dir}/auth/
"""

    with open(db_backup_script, 'w') as f:
        f.write(db_backup_content)
    os.chmod(db_backup_script, 0o755)
    logging.info(f"Created and set permissions for: {db_backup_script}")

    with open(auth_backup_script, 'w') as f:
        f.write(auth_backup_content)
    os.chmod(auth_backup_script, 0o755)
    logging.info(f"Created and set permissions for: {auth_backup_script}")



# Takes script path as argument and runs it
# Prints standard output/error
def run_backup(script_path):
    try:
        result = subprocess.run([script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logging.info(f"Running backup script: {script_path}")
        logging.info(f"Output: {result.stdout.decode('utf-8')}")
        logging.info(f"Error (if any): {result.stderr.decode('utf-8')}")
    except FileNotFoundError:
        logging.error(f"Error: Backup script {script_path} not found.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

# Defines the path to the database backup script
def backup_db():
    script_path = os.path.join(backup_scripts_dir, 'backup_db.sh')
    return run_backup(script_path)

# Defines path to authentication server backup script
def backup_auth():
    script_path = os.path.join(backup_scripts_dir, 'backup_auth.sh')
    return run_backup(script_path)

# Function to monitor system performance
def monitor_system(server_name):
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk_usage = psutil.disk_usage('/')
    logging.info(f"{server_name} CPU Usage: {cpu_usage}%")
    logging.info(f"{server_name} Memory Usage: {memory.percent}%")
    logging.info(f"{server_name} Disk Usage: {disk_usage.percent}%")
    print(f"{server_name} CPU Usage: {cpu_usage}%")
    print(f"{server_name} Memory Usage: {memory.percent}%")
    print(f"{server_name} Disk Usage: {disk_usage.percent}%")

# Main entry point
if __name__ == '__main__':
    logging.info(f"Command-line arguments: {sys.argv}")
    # Ensures the command has exactly two arguments
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        # Error is thrown, with a message 
        logging.error("Please type: python3 app.py <create_scripts|backup_db|backup_auth|monitor> <server_name>")
        sys.exit(1)
    
    # Sees if user wants to create the scripts, back up the database, or the authentication server
    command = sys.argv[1]
    server_name = sys.argv[2] if len(sys.argv) == 3 else None
    logging.info(f"Command received: {command}")

    if command == 'create_scripts':
        create_backup_scripts()
        logging.info("Backup scripts created successfully.")
    elif command == 'backup_db':
        backup_db()
    elif command == 'backup_auth':
        backup_auth()
    elif command == 'monitor' and server_name:
        monitor_system(server_name)
    else:
        logging.error("Invalid command. Use 'create_scripts', 'backup_db', 'backup_auth', or 'monitor <server_name>'.")