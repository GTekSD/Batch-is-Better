#!/usr/bin/env python3

# Author: Сухас Дхолз
# Link: https://github.com/GTekSD/
# Copyright (C) 2024, GTekSD Developers.
# See the LICENSE file for copying permission.

import os
import sys
import subprocess

# Function to display the banner
def banner():
    print(" ")
    print("       \033[32mW\033[0m \033[33m____        __       __  \033[0m         \033[32m  \      , \033[0m       ")
    print(" \033[32mW    WW\033[0m\033[33m/ __ )____ _/ /______/ /_ \033[0m  \033[1m  v1.0\033[0m  \033[32m  l\   ,/   \033[0m      ")
    print(" \033[32mWWW  W\033[0m\033[33m/ __  / __ ^/ __/ ___/ __ \  _ \033[0m \033[32m ._   ^|] /j     \033[0m     ")
    print("  \033[32mWWW\033[0m \033[33m/ /_/ / /_/ / /_/ /__/ / / / (_)____\033[0m\033[32m\\, \|w7 _,/^  \033[0m    ")
    print("   \033[32mWW\033[0m\033[33m/_____/\__,__\___\___/_/ /_/ / / ___/\033[0m \033[32m^^=,e/,x-^    \033[0m    ")
    print("  \033[32mWW\033[0m\033[33m/ __ )___  / /_/ /____  _____/ (__  )\033[0m  \033[32m ,z/eY-=-    \033[0m     ")
    print(" \033[32mW\033[0m \033[33m/ __  / _ \/ __/ __/ _ \/ ___/_/____/\033[0m \033[32m -^^ .d \    \033[0m       ")
    print("\033[33m  / /_/ /  __/ /_/ /_/  __/ /\033[0m \033[1;92mCODED BY\033[0m       \033[32m '   \    \033[0m      ")
    print("\033[33m /_____/\___/\__/\__/\___/_/\033[0m \033[1;92mСухас Дхолз WITH ❤ FOR GTekSD\033[0m  ") 
    print(" ")

# Function to display usage information
def usage():
    banner()
    print("[i] Usage: bisb <command> <filename.txt>")
    print(" |         bisb <\"command -x -y -z\"> <filename.txt>  ")
    print(" +-----------------------------------------------------------")
    print(" | Examples:")
    print(" | ")
    print(" | 1. System Administration:")
    print(" | \033[32m└─\033[0m\033[34m$\033[0m \033[2;34mbisb\033[0m \033[32m\"sudo systemctl restart service\"\033[0m server_list.txt")
    print(" |")
    print(" | 2. Data Processing:")
    print(" | \033[32m└─\033[0m\033[34m$\033[0m \033[2;34mbisb\033[0m \033[32m\"python process_data.py\"\033[0m data_files.txt")
    print(" |")
    print(" | 3. Configuration Management:")
    print(" | \033[32m└─\033[0m\033[34m$\033[0m \033[2;34mbisb\033[0m \033[32m\"ansible-playbook deploy.yml\"\033[0m environments.txt")
    print(" |")
    print(" | 4. File Management:")
    print(" | \033[32m└─\033[0m\033[34m$\033[0m \033[2;34mbisb\033[0m \033[32m\"mv\"\033[0m files_to_move.txt")
    print(" |")
    print(" | 5. Testing and Validation:")
    print(" | \033[32m└─\033[0m\033[34m$\033[0m \033[2;34mbisb\033[0m \033[32m\"pytest --verbose\"\033[0m test_cases.txt")
    print(" |")
    print(" | 6. Script Execution on Remote Machines:")
    print(" | \033[32m└─\033[0m\033[34m$\033[0m \033[2;34mbisb\033[0m \033[32m\"ssh user@hostname 'bash -s'\"\033[0m remote_commands.txt")
    print(" |")
    print(" | 7. Database Operations:")
    print(" | \033[32m└─\033[0m\033[34m$\033[0m \033[2;34mbisb\033[0m \033[32m\"mysql -u root -p<password> -e 'SELECT * FROM table'\"\033[0m databases.txt")
    print(" |")
    print(" | 8. Image Processing:")
    print(" | \033[32m└─\033[0m\033[34m$\033[0m \033[2;34mbisb\033[0m \033[32m\"convert -resize 50% image.jpg\"\033[0m image_list.txt")
    print(" |")
    print(" | 9. Text Processing:")
    print(" | \033[32m└─\033[0m\033[34m$\033[0m \033[2;34mbisb\033[0m \033[32m\"grep 'error' log_file.txt\"\033[0m log_files.txt")
    print(" |")
    print(" | 10. File Compression and Archiving:")
    print(" | \033[32m└─\033[0m\033[34m$\033[0m \033[2;34mbisb\033[0m \033[32m\"tar -czvf archive.tar.gz folder\"\033[0m folders_to_archive.txt")
    print(" |")
    print(" | 11. Deployment Automation:")
    print(" | \033[32m└─\033[0m\033[34m$\033[0m \033[2;34mbisb\033[0m \033[32m\"deploy_script.sh\"\033[0m servers.txt")
    print(" |")
    print(" | 12. Monitoring and Reporting:")
    print(" | \033[32m└─\033[0m\033[34m$\033[0m \033[2;34mbisb\033[0m \033[32m\"top -n 1 -b\"\033[0m servers_list.txt")
    print(" |")
    print(" | 13. Configuration Updates:")
    print(" | \033[32m└─\033[0m\033[34m$\033[0m \033[2;34mbisb\033[0m \033[32m\"sed -i 's/old_value/new_value/g' config_file.conf\"\033[0m nodes_list.txt")
    print(" |")
    print(" | 14. Script Distribution:")
    print(" | \033[32m└─\033[0m\033[34m$\033[0m \033[2;34mbisb\033[0m \033[32m\"scp script.sh user@client:/path/to/destination/\"\033[0m clients_list.txt")
    print(" |")
    print(" | 15. Network Operations:")
    print(" | \033[32m└─\033[0m\033[34m$\33[2;34mbisb\033[0m \033[32m\"ping -c 3 server\"\033[0m network_devices.txt")
    print(" +-----------------------------------------------------------")
    sys.exit(1)

# Main function to parse arguments and execute commands
def main():
    if len(sys.argv) == 2 and sys.argv[1] in ('-h', '--help'):
        usage()
    elif len(sys.argv) != 3:
        print("[!] U Fo0l: Invalid number of arguments.")
        print("[i] Use -h or --help for usage information.")
        sys.exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    if not os.path.isfile(filename):
        print(f"[!] Sh!T: File '{filename}' not found.")
        print("[i] Use -h or --help for usage information.")
        sys.exit(1)

    with open(filename, 'r') as file:
        for line in file:
            full_command = f"{command} {line.strip()}"
            print("\n[i] Executing:", full_command)
            print(" +------------ - ")
            subprocess.run(full_command, shell=True)

if __name__ == "__main__":
    main()
