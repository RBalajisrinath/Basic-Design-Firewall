# Math Bc Firewall

This project implements a basic firewall to protect a Math Bc server against Denial of Service (DoS) attacks. It includes a simulation to demonstrate the firewall's functionality.

## Features

- Analyzes incoming network traffic to identify potential DoS attacks
- Detects excessive traffic from single IP addresses
- Blocks IP addresses that exceed the request limit
- Logs all detected DoS attacks for further analysis
- Includes a simulation of a Math Bc server to demonstrate the firewall in action

## Requirements

- Python 3.6 or higher

## Installation

1. Clone this repository or download the `math_bc_firewall.py` file.
2. No additional libraries are required as the script uses only Python standard libraries.

## Usage

To run the Math Bc Firewall simulation:

1. Open a terminal or command prompt.
2. Navigate to the directory containing `math_bc_firewall.py`.
3. Run the following command:

   ```
   python math_bc_firewall.py
   ```

4. The simulation will run for approximately 2 minutes, showing output in the console.
5. After the simulation completes, check the `firewall.log` file in the same directory for detailed logs.

## Configuration

You can modify the following parameters in the `math_bc_firewall.py` file to adjust the firewall's behavior:

- `request_limit`: Maximum number of requests allowed from a single IP within the time window
- `time_window`: Time period (in seconds) for counting requests
- `block_duration`: Duration (in seconds) for which an IP is blocked after exceeding the limit

To change these parameters, modify the `Firewall` initialization in the `__main__` section of the script:
