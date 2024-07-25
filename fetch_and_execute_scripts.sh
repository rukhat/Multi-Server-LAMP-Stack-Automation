#!/bin/bash

echo "Starting Script"

# Configuration
DB_HOST="192.168.56.10"
DB_USER="demo_user"
DB_PASS="team3"
DB_NAME="myapp"

echo "Fetching Path"

# Fetch script paths from database
fetch_script_paths() {
    mysql -h "$DB_HOST" -u "$DB_USER" -p"$DB_PASS" "$DB_NAME" -N -e "SELECT name, file_path FROM scripts"
}

# Execute remote script
execute_remote_script() {
    local name=$1
    local file_path=$2
    echo "Executing $name:"
    ssh vagrant@$DB_HOST "bash $file_path"
}

# Main execution
main() {
    while IFS=$'\t' read -r name file_path; do
        execute_remote_script "$name" "$file_path"
    done < <(fetch_script_paths)

    echo "Done"
}

main