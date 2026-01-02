# SIP Gateway Auto-Configuration Tool

Automated login and configuration tool for SIP Gateway devices using Python and Selenium.

## Overview

This tool automates the process of logging into a SIP Gateway web interface and configuring it for SIP client registration and phone call functionality. The script probes all configuration pages, identifies required parameters, and interactively prompts the user for values with helpful examples.

## Features

- **Automated Login**: Automatically logs into the SIP Gateway web interface
- **Configuration Probing**: Scans all configuration pages to identify required parameters
- **Interactive Configuration**: Prompts user for each parameter with examples and current values
- **Smart Field Detection**: Automatically detects input fields, select boxes, checkboxes, and textareas
- **SSL/TLS Support**: Handles self-signed certificates (common in gateway devices)
- **Configuration Application**: Automatically fills and submits all configuration forms

## Prerequisites

- Python 3.7 or higher
- Google Chrome browser
- ChromeDriver (automatically managed by Selenium 4.15+)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/andycheng11233/sipgateway.git
cd sipgateway
```

2. Create a virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

Run the script with default settings:

```bash
python sip_gateway_config.py
```

Default settings:
- Gateway URL: `https://192.168.1.122:31567`
- Username: `admin`
- Password: `Abcd--1234`

The script will:
1. Log into the gateway
2. Probe all configuration pages
3. Display found configuration fields with examples
4. Prompt you for values (press Enter to skip any field)
5. Apply the configuration automatically

### Custom Gateway Settings

When prompted, you can change the default gateway URL, username, and password.

### Configuration Pages

The script probes the following configuration pages:
- `/cgi-bin/config2` - General configuration
- `/cgi-bin/config` - Basic settings
- `/cgi-bin/config_a1` - Account 1 settings
- `/cgi-bin/config_a2` - Account 2 settings
- `/cgi-bin/config_dns` - DNS settings

## Configuration Examples

The script provides examples for common SIP parameters:

### Network Settings
- **IP Address**: e.g., `192.168.1.100`
- **Netmask**: e.g., `255.255.255.0`
- **Gateway**: e.g., `192.168.1.1`
- **DNS Servers**: e.g., `8.8.8.8`, `8.8.4.4`

### SIP Server Settings
- **SIP Server**: e.g., `sip.example.com`
- **SIP Port**: e.g., `5060`
- **SIP Domain**: e.g., `example.com`

### SIP Account Settings
- **Username**: e.g., `user1000`
- **Display Name**: e.g., `User 1000`
- **Password**: Your SIP account password
- **Extension**: e.g., `1000`

### Advanced Settings
- **Codecs**: e.g., `ulaw,alaw,g729`
- **DTMF Mode**: e.g., `rfc2833`
- **RTP Ports**: e.g., `10000-20000`

## After Configuration

Once configuration is complete, you can use any SIP client to register:

1. **Choose a SIP Client**:
   - **Desktop**: Zoiper, X-Lite, Jitsi
   - **Mobile**: Zoiper, Linphone, Bria
   - **Web**: JsSIP-based clients

2. **Configure Your SIP Client**:
   - Use the SIP server address you configured
   - Enter your username/extension
   - Enter your password
   - Set the port (usually 5060 for SIP)

3. **Make/Receive Calls**:
   - After registration, you should be able to make and receive calls
   - The gateway will handle the SIP signaling and RTP media

## Troubleshooting

### ChromeDriver Issues
If you encounter ChromeDriver issues:
```bash
# Install/update ChromeDriver
pip install --upgrade selenium
```

### SSL Certificate Errors
The script handles self-signed certificates automatically. If you still encounter issues, check that the gateway is accessible from your network.

### Login Failures
- Verify the gateway URL is correct and accessible
- Check username and password
- Ensure the gateway web interface is running

### Configuration Not Applied
- Check that you have proper permissions on the gateway
- Verify the gateway accepts the configuration format
- Look at browser window (if not headless) to see any error messages

## Development

### Running in Headless Mode
To run without opening a browser window, uncomment this line in `sip_gateway_config.py`:
```python
# chrome_options.add_argument('--headless')
```

### Adding More Configuration Pages
To probe additional pages, add URLs to the `config_pages` list in the `run_configuration_workflow()` method.

## Requirements

See `requirements.txt` for complete dependency list:
- selenium>=4.15.0 - Web automation framework
- urllib3>=2.0.0 - HTTP client with SSL support

## Security Notes

- The script disables SSL certificate verification for self-signed certificates
- Credentials are not stored or transmitted to external services
- Configuration data remains local to your system
- Review the script before running if you have security concerns

## License

This project is open source and available for use in configuring SIP gateway devices.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

## Support

For issues or questions:
1. Check the Troubleshooting section above
2. Open an issue on GitHub
3. Review the SIP Gateway device documentation

## Disclaimer

This tool is designed for legitimate configuration of devices you own or have permission to configure. Always ensure you have proper authorization before using this tool.
