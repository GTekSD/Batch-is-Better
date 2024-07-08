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
