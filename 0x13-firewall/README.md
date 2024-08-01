# Firewall Configuration with ufw

This repository contains scripts and configurations for configuring the ufw firewall on `web-01`.

## Description

The scripts provided here are used to configure the ufw firewall on `web-01` according to specific requirements. These configurations include blocking all incoming traffic except for SSH (port 22), HTTPS (port 443), and HTTP (port 80), as well as setting up port forwarding from port 8080 to port 80.

## Files

- `0-block_all_incoming_traffic_but`: Script to block all incoming traffic except specified ports.
- `100-port_forwarding`: Script to forward port 8080 to port 80 using ufw.

## Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/alx-system_engineering-devops.git

