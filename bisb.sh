#!/bin/bash

# Author: Сухас Дхолз
# Link: https://github.com/GTekSD/
# Copyright (C) 2024, GTekSD Developers.
# See the LICENSE file for copying permission.

# Function to display the banner
banner() {
    echo " "
    echo "       \033[32mW\033[0m \033[33m____        __       __  \033[0m         \033[32m  \      , \033[0m       "
    echo " \033[32mW    WW\033[0m\033[33m/ __ )____ _/ /______/ /_ \033[0m  \033[1m  v1.0\033[0m  \033[32m  l\   ,/   \033[0m      "
    echo " \033[32mWWW  W\033[0m\033[33m/ __  / __ ^/ __/ ___/ __ \  _ \033[0m \033[32m ._   ^|] /j     \033[0m     "
    echo "  \033[32mWWW\033[0m \033[33m/ /_/ / /_/ / /_/ /__/ / / / (_)____\033[0m\033[32m\\, \|w7 _,/^  \033[0m    "
    echo "   \033[32mWW\033[0m\033[33m/_____/\__,__\___\___/_/ /_/ / / ___/\033[0m \033[32m^^=,e/,x-^    \033[0m    "
    echo "  \033[32mWW\033[0m\033[33m/ __ )___  / /_/ /____  _____/ (__  )\033[0m  \033[32m ,z/eY-=-    \033[0m     "
    echo " \033[32mW\033[0m \033[33m/ __  / _ \/ __/ __/ _ \/ ___/_/____/\033[0m \033[32m -^^ .d \    \033[0m       "
    echo "\033[33m  / /_/ /  __/ /_/ /_/  __/ /\033[0m \033[1;92mCODED BY\033[0m       \033[32m '   \    \033[0m      "
    echo "\033[33m /_____/\___/\__/\__/\___/_/\033[0m \033[1;92mСухас Дхолз WITH ❤ FOR GTekSD\033[0m  " 
    echo " "
}


# Function to display usage information
usage() {
    banner
    echo "[i] Usage: $0 <command> <filename.txt>"
    echo " |         $0 <\"command -x -y -z\"> <filename.txt>  "
    echo " +-----------------------------------------------------------"
    echo " | Examples:"
    echo " | "
    echo " | 1. System Administration:"
    echo " | \033[32m└─\033[0m\033[34m$\033[0m \033[2;34m$0\033[0m \033[32m\"sudo systemctl restart service\"\033[0m server_list.txt"
    echo " |"
    echo " | 2. Data Processing:"
    echo " | \033[32m└─\033[0m\033[34m$\033[0m \033[2;34m$0\033[0m \033[32m\"python process_data.py\"\033[0m data_files.txt"
    echo " |"
    echo " | 3. Configuration Management:"
    echo " | \033[32m└─\033[0m\033[34m$\033[0m \033[2;34m$0\033[0m \033[32m\"ansible-playbook deploy.yml\"\033[0m environments.txt"
    echo " |"
    echo " | 4. File Management:"
    echo " | \033[32m└─\033[0m\033[34m$\033[0m \033[2;34m$0\033[0m \033[32m\"mv\"\033[0m files_to_move.txt"
    echo " |"
    echo " | 5. Testing and Validation:"
    echo " | \033[32m└─\033[0m\033[34m$\033[0m \033[2;34m$0\033[0m \033[32m\"pytest --verbose\"\033[0m test_cases.txt"
    echo " |"
    echo " | 6. Script Execution on Remote Machines:"
    echo " | \033[32m└─\033[0m\033[34m$\033[0m \033[2;34m$0\033[0m \033[32m\"ssh user@hostname 'bash -s'\"\033[0m remote_commands.txt"
    echo " |"
    echo " | 7. Database Operations:"
    echo " | \033[32m└─\033[0m\033[34m$\033[0m \033[2;34m$0\033[0m \033[32m\"mysql -u root -p<password> -e 'SELECT * FROM table'\"\033[0m databases.txt"
    echo " |"
    echo " | 8. Image Processing:"
    echo " | \033[32m└─\033[0m\033[34m$\033[0m \033[2;34m$0\033[0m \033[32m\"convert -resize 50% image.jpg\"\033[0m image_list.txt"
    echo " |"
    echo " | 9. Text Processing:"
    echo " | \033[32m└─\033[0m\033[34m$\033[0m \033[2;34m$0\033[0m \033[32m\"grep 'error' log_file.txt\"\033[0m log_files.txt"
    echo " |"
    echo " | 10. File Compression and Archiving:"
    echo " | \033[32m└─\033[0m\033[34m$\033[0m \033[2;34m$0\033[0m \033[32m\"tar -czvf archive.tar.gz folder\"\033[0m folders_to_archive.txt"
    echo " |"
    echo " | 11. Deployment Automation:"
    echo " | \033[32m└─\033[0m\033[34m$\033[0m \033[2;34m$0\033[0m \033[32m\"deploy_script.sh\"\033[0m servers.txt"
    echo " |"
    echo " | 12. Monitoring and Reporting:"
    echo " | \033[32m└─\033[0m\033[34m$\033[0m \033[2;34m$0\033[0m \033[32m\"top -n 1 -b\"\033[0m servers_list.txt"
    echo " |"
    echo " | 13. Configuration Updates:"
    echo " | \033[32m└─\033[0m\033[34m$\033[0m \033[2;34m$0\033[0m \033[32m\"sed -i 's/old_value/new_value/g' config_file.conf\"\033[0m nodes_list.txt"
    echo " |"
    echo " | 14. Script Distribution:"
    echo " | \033[32m└─\033[0m\033[34m$\033[0m \033[2;34m$0\033[0m \033[32m\"scp script.sh user@client:/path/to/destination/\"\033[0m clients_list.txt"
    echo " |"
    echo " | 15. Network Operations:"
    echo " | \033[32m└─\033[0m\033[34m$\033[0m \033[2;34m$0\033[0m \033[32m\"ping -c 3 server\"\033[0m network_devices.txt"
    echo " +-----------------------------------------------------------"
    exit 1
}

# Check if the help argument is provided
if [ "$#" -eq 1 ] && { [ "$1" = "-h" ] || [ "$1" = "--help" ]; }; then
    usage
elif [ "$#" -ne 2 ]; then
    echo "[!] U Fo0l: Invalid number of arguments."
    echo "[i] Use -h or --help for usage information."
    exit 1
fi

command="$1"
filename="$2"

if [ ! -f "$filename" ]; then
    echo "[!] Sh!T: File '$filename' not found."
    echo "[i] Use -h or --help for usage information."
    exit 1
fi

while IFS= read -r line; do
    full_command="$command $line"
    echo ""
    echo "[i] Executing: $full_command"
    echo " +------------ - "
    eval "$full_command"
done < "$filename"
