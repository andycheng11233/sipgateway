# SIP Gateway Configuration Guide

## What You'll Need

Before running the configuration script, gather the following information from your SIP service provider or VoIP administrator:

## Essential Information

### 1. SIP Server Information
- **SIP Server Address**: The hostname or IP of your SIP server
  - Example: `sip.voip-provider.com` or `192.168.1.50`
- **SIP Port**: Usually `5060` (UDP) or `5061` (TLS)
- **SIP Domain**: Your SIP domain
  - Example: `voip-provider.com`

### 2. Account Credentials
- **Username/Account ID**: Your SIP account username
  - Example: `1000` or `user1000`
- **Password**: Your SIP account password
- **Display Name**: How you want to appear on caller ID
  - Example: `John Doe` or `Office Phone`

### 3. Network Settings (if using static IP)
- **IP Address**: The IP for your gateway
  - Example: `192.168.1.100`
- **Subnet Mask**: Usually `255.255.255.0`
- **Gateway**: Your network gateway/router
  - Example: `192.168.1.1`
- **DNS Servers**: 
  - Primary: `8.8.8.8` (Google) or your ISP's DNS
  - Secondary: `8.8.4.4` or `1.1.1.1` (Cloudflare)

## Running the Configuration

### Step 1: Start the Script
```bash
python sip_gateway_config.py
```

Or use the quick start script:
```bash
./quick_start.sh        # Linux/Mac
quick_start.bat         # Windows
```

### Step 2: Login
The script will automatically log in with the credentials:
- URL: `https://192.168.1.122:31567`
- Username: `admin`
- Password: `Abcd--1234`

If your gateway uses different credentials, answer 'n' when asked if you want to use default settings.

### Step 3: Answer Configuration Prompts

The script will probe the configuration pages and ask for values. Here's what to expect:

#### Network Configuration (if prompted)
```
IP Address (e.g., 192.168.1.100): 192.168.1.100
Netmask (e.g., 255.255.255.0): 255.255.255.0
Gateway (e.g., 192.168.1.1): 192.168.1.1
```

#### DNS Configuration
```
Primary DNS (e.g., 8.8.8.8): 8.8.8.8
Secondary DNS (e.g., 8.8.4.4): 8.8.4.4
```

#### SIP Server Configuration
```
SIP Server (e.g., sip.example.com): sip.myvoipprovider.com
SIP Port (e.g., 5060): 5060
SIP Domain (e.g., example.com): myvoipprovider.com
```

#### Account Configuration
```
Username (e.g., user1000): 1000
Password [password]: your_sip_password_here
Display Name (e.g., User 1000): John Doe
Extension (e.g., 1000): 1000
```

#### Codec Configuration (if prompted)
```
Codec Priority (e.g., ulaw,alaw,g729): ulaw,alaw
DTMF Mode (e.g., rfc2833): rfc2833
```

### Step 4: Review and Confirm
After entering all values, the script will:
1. Apply the configuration to the gateway
2. Submit the forms automatically
3. Display a summary of what was configured

### Step 5: Test Your Configuration

After configuration is complete, test with a SIP client:

#### Recommended SIP Clients
- **Windows**: Zoiper, X-Lite, MicroSIP
- **macOS**: Zoiper, Telephone, X-Lite
- **Linux**: Linphone, Jitsi, Ekiga
- **iOS**: Zoiper, Linphone, Bria
- **Android**: Zoiper, Linphone, CSipSimple

#### Configure Your SIP Client
1. Open your SIP client
2. Add a new account with:
   - Server: The SIP server you configured
   - Username: The username you configured
   - Password: The password you configured
   - Port: Usually 5060

3. Save and register the account

4. Once registered (usually shows as "Online" or "Registered"), you can:
   - Make calls by dialing another extension or phone number
   - Receive calls on your extension

## Common Configuration Scenarios

### Scenario 1: Basic Home Setup
```
SIP Server: Your VoIP provider's server
Username: Your phone number or extension
Password: Provider-given password
Network: DHCP (leave IP fields empty)
```

### Scenario 2: Office PBX
```
SIP Server: Internal PBX IP (e.g., 192.168.1.50)
Username: Extension number (e.g., 1001)
Password: Extension password
Network: Static IP on local network
```

### Scenario 3: Cloud SIP Provider
```
SIP Server: Provider's cloud server (e.g., sip.provider.com)
Username: Account ID from provider
Password: Account password from provider
Network: DHCP or Static, depends on your network
```

## Troubleshooting

### Registration Failed
1. Double-check server address, username, and password
2. Verify port is correct (usually 5060)
3. Check firewall settings
4. Ensure gateway has internet access

### Cannot Make Calls
1. Verify registration is successful
2. Check codec compatibility
3. Ensure RTP ports are not blocked (usually 10000-20000)
4. Check account has calling permissions

### One-Way Audio
1. Check firewall/NAT settings
2. Configure STUN server if behind NAT
3. Verify RTP port range is correct and open

### Cannot Receive Calls
1. Verify registration is active
2. Check inbound route configuration on PBX/server
3. Ensure extension/DID is correctly set up

## Additional Resources

- Check your SIP provider's documentation for specific settings
- Review your gateway's manual for advanced features
- Test with a known working SIP client before configuring
- Keep a backup of working configuration

## Need Help?

If you're unsure about specific values:
1. Press Enter to skip the field during configuration
2. Contact your SIP service provider or VoIP administrator
3. Check the gateway's current configuration through the web interface
4. Refer to the provider's setup guide or documentation

## Security Tips

- Change default gateway passwords
- Use strong SIP account passwords
- Enable TLS/SRTP if supported by your provider
- Restrict access to the gateway's web interface
- Keep the gateway firmware updated
- Use firewall rules to limit access
