# Grandstream HT813 SIP Gateway Configuration Guide

## Overview
This guide will help you configure your Grandstream HT813 Analog Telephone Adapter (ATA) for use as a home SIP gateway with an analog FXO line.

### HT813 Features
- **1 FXS Port**: Connect analog phones/fax machines to make calls via SIP
- **1 FXO Port**: Connect to PSTN (analog phone line) to route calls through traditional phone line
- **Dual SIP accounts**: Support for multiple VoIP providers
- **NAT traversal**: Works behind home routers
- **T.38 Fax support**: Reliable fax over IP

---

## Before You Begin

### Information You Need to Gather

#### From Your SIP/VoIP Provider:
1. **SIP Server Address** (e.g., sip.yourprovider.com or IP address)
2. **SIP User ID / Account Name**
3. **Authentication ID** (if different from User ID)
4. **Password**
5. **SIP Port** (usually 5060 or 5061 for TLS)
6. **Transport Protocol** (UDP, TCP, or TLS)
7. **Registration Expiration** (typically 60-3600 seconds)
8. **Outbound Proxy** (if required by provider)

#### Your Network Information:
1. **Static IP or DHCP**: How you want the HT813 to get its IP
2. **Your Router's IP**: For default gateway
3. **DNS Servers**: Usually your ISP's DNS or public DNS (8.8.8.8)
4. **Port Forwarding**: May be needed for RTP ports

#### Your Phone Setup:
1. **Phone Number(s)**: The phone number(s) you want to use
2. **Analog Devices**: What you're connecting (phone, fax machine)
3. **Call Routing Preferences**: How you want calls to be routed

---

## Initial Setup

### Step 1: Physical Connections
1. **Power**: Connect the power adapter
2. **Network**: Connect Ethernet cable from HT813 LAN port to your router
3. **FXO Port**: Connect to your PSTN line (wall jack) - **LINE port**
4. **FXS Port**: Connect your analog phone - **PHONE port**

### Step 2: Find the Device IP Address
1. Pick up the analog phone connected to the FXS port
2. Dial `***` followed by `02` (IVR menu code)
3. The device will announce its IP address
4. Alternatively, check your router's DHCP client list

### Step 3: Access Web Interface
1. Open a web browser
2. Navigate to `http://[HT813_IP_ADDRESS]`
3. Default login credentials:
   - **Username**: `admin`
   - **Password**: `admin`
4. **IMPORTANT**: Change the default password immediately!

---

## Configuration Sections

### Basic Network Settings

**Navigation**: Basic Settings → Network Settings

| Parameter | Recommended Value | Notes |
|-----------|------------------|-------|
| Internet Connection Type | DHCP | Use Static if you need fixed IP |
| IP Address | Auto (DHCP) | Or set static IP |
| Subnet Mask | Auto (DHCP) | Or 255.255.255.0 for static |
| Default Router | Auto (DHCP) | Your router's IP for static |
| DNS Server 1 | Auto (DHCP) | Or 8.8.8.8 (Google DNS) |
| DNS Server 2 | Auto (DHCP) | Or 8.8.4.4 |
| Preferred DNS Server | 8.8.8.8 | Public DNS recommended |
| Layer 3 QoS | 48 | For voice traffic priority |
| Enable LLDP | No | Unless required by network |

### FXS Port Configuration (PHONE Port)

**Navigation**: FXS PORT → FXS Port Settings

**Account Configuration:**

| Parameter | Your Value | Example / Notes |
|-----------|-----------|-----------------|
| Account Active | Yes | Enable the account |
| Primary SIP Server | `[TO FILL]` | sip.yourprovider.com |
| Failover SIP Server | `[TO FILL]` | Optional backup server |
| Outbound Proxy | `[TO FILL]` | If required by provider |
| SIP User ID | `[TO FILL]` | Your SIP username |
| Authenticate ID | `[TO FILL]` | Usually same as User ID |
| Authenticate Password | `[TO FILL]` | Your SIP password |
| Name | `[TO FILL]` | Your display name |
| SIP Registration | Yes | Must be Yes for most providers |
| Unregister On Reboot | No | Keep registered |
| SIP Transport | UDP | Or TCP/TLS per provider |
| NAT Traversal | Keep-Alive | Or STUN if needed |

**Audio Settings:**

| Parameter | Recommended Value | Notes |
|-----------|------------------|-------|
| Preferred Vocoder | PCMU, PCMA, G729 | Check provider support |
| Use First Matching Vocoder | Yes | Faster codec negotiation |
| VAD | No | Voice Activity Detection |
| Jitter Buffer Type | Adaptive | Best for varying conditions |

**Dial Plan:**
```
{ x+ | \+x+ | *x+ | *xx*x+ }
```
This allows:
- Local extensions (x+)
- International format (+x+)
- Star codes (*x+)
- Feature codes (*xx*x+)

### FXO Port Configuration (LINE Port)

**Navigation**: FXO PORT → FXO Port Settings

**Basic FXO Settings:**

| Parameter | Recommended Value | Notes |
|-----------|------------------|-------|
| Enable FXO Port | Yes | Enable to use PSTN line |
| Ring Thru FXS Port | No | Unless you want phone to ring |
| Loop Current Disconnection | Yes | Detect when PSTN call ends |
| Caller ID Scheme | Bellcore/Telcordia | For USA, adjust for country |
| Caller ID Type | DTMF | Or FSK depending on region |
| Impedance | 600 ohm | Match your country (USA: 600) |
| Disconnect Tone | Enabled | Detect busy/disconnect tones |
| PSTN Caller Default | Yes | Route unknown callers to PSTN |

**FXO to SIP Routing:**

| Parameter | Your Value | Notes |
|-----------|-----------|-------|
| FXO Failover | Enable | Forward to SIP when PSTN fails |
| Primary SIP Account | Account 1 | Route calls to this SIP account |
| Offhook Auto-Dial | `[TO FILL]` | Auto-dial this number on offhook |
| Hotline Number | `[TO FILL]` | Optional: always dial this number |

**Dial Plan for FXO to SIP:**
```
{ x+ | \+x+ }
```
Routes all calls from PSTN to SIP

### Call Routing Strategy

**Option 1: PSTN Backup (Recommended for beginners)**
- Use SIP as primary for outbound calls
- FXO as backup when SIP fails
- Incoming PSTN calls forwarded to FXS phone

**Option 2: Selective Routing**
- Local calls via PSTN (cheaper)
- Long distance via SIP (VoIP savings)
- Requires custom dial plan

**Option 3: SIP-to-PSTN Bridge**
- All calls route through SIP
- FXO only for incoming PSTN calls
- Maximum VoIP utilization

### Advanced Dial Plan Examples

**Route local calls (7 digits) via PSTN, others via SIP:**
```
FXS Dial Plan: { Lxxx xxxx:xx. | x+ | \+x+ }
```
Where `L` prefix routes to PSTN line

**International call support:**
```
{ 011xx. | 00xx. | x+ | \+x+ }
```
Allows 011 (US intl) or 00 (European intl) prefixes

**Emergency services priority:**
```
{ 911 | 112 | x+ }
```
Always ensure emergency numbers work!

### SIP Advanced Settings

**Navigation**: FXS PORT → SIP Settings (Advanced)

| Parameter | Recommended Value | Notes |
|-----------|------------------|-------|
| SIP Registration Expiration | 60 | Seconds, adjust per provider |
| SIP T1 Timeout | 0.5 | Seconds |
| SIP T2 Timeout | 4 | Seconds |
| Session Timer | Yes | Keep calls alive through NAT |
| Local SIP Port | 5060 | Default SIP port |
| Local RTP Port | 5004 | Starting RTP port |
| Use Random Port | No | Better for debugging |
| Keep-alive Interval | 20 | Seconds, for NAT traversal |
| STUN Server | stun.l.google.com | If NAT traversal needs STUN |

---

## Testing Your Configuration

### Test 1: FXS Port (Analog Phone)
1. Pick up the phone connected to FXS port
2. Listen for dial tone
3. Dial a test number
4. Verify call goes through SIP provider

### Test 2: FXO Port (PSTN Line)
1. Call your PSTN line from another phone
2. Verify the call is received
3. Check if it routes correctly (to FXS phone or SIP)

### Test 3: Audio Quality
1. Make a test call
2. Check both directions of audio
3. Verify no echo, delay, or cutting out
4. Adjust codecs if quality issues

### Test 4: Fax (if applicable)
1. Send a test fax
2. Enable T.38 if fax over IP is used
3. Verify fax quality

---

## Troubleshooting

### Issue: No Registration to SIP Server
**Symptoms**: Can't make calls, "Service Unavailable" message

**Solutions**:
1. Check SIP credentials (User ID, Password)
2. Verify SIP server address is correct
3. Check NAT traversal settings
4. Ensure router allows SIP port (5060/5061)
5. Check SIP provider status

### Issue: One-Way Audio
**Symptoms**: You can hear them, they can't hear you (or vice versa)

**Solutions**:
1. Enable STUN server
2. Forward RTP ports (5004-5082) in router
3. Check firewall settings
4. Enable "Symmetric RTP"
5. Try different NAT traversal methods

### Issue: No Dial Tone on FXS Port
**Symptoms**: Pick up phone, no dial tone

**Solutions**:
1. Verify FXS port is enabled
2. Check SIP registration status
3. Ensure account is active
4. Test with different phone

### Issue: FXO Port Not Detecting PSTN Line
**Symptoms**: No incoming calls from PSTN

**Solutions**:
1. Verify FXO port is enabled
2. Check impedance setting matches your country
3. Verify physical connection to wall jack
4. Test with known working PSTN line
5. Adjust voltage threshold

### Issue: Dropped Calls
**Symptoms**: Calls disconnect unexpectedly

**Solutions**:
1. Enable Session Timer
2. Increase SIP registration expiration
3. Enable Keep-alive packets
4. Check network stability
5. Verify QoS settings

### Issue: Echo on Calls
**Symptoms**: Hear your own voice with delay

**Solutions**:
1. Enable echo cancellation
2. Adjust echo cancellation tail length
3. Check impedance settings
4. Reduce audio levels
5. Try different codecs

---

## Security Best Practices

1. **Change Default Password**: First thing after login!
2. **Firmware Updates**: Keep HT813 firmware up to date
3. **Strong SIP Password**: Use complex password from provider
4. **Disable Unused Features**: Turn off services you don't need
5. **Access Control**: Limit web access to local network only
6. **Use TLS**: If provider supports, use encrypted SIP (port 5061)
7. **Admin IP Restrictions**: Whitelist IP addresses for web interface

---

## Quick Reference: IVR Menu Codes

Dial these codes from the analog phone connected to FXS port:

- `***` - Enter IVR menu
- `*** 02` - Hear IP address
- `*** 03` - Hear MAC address
- `*** 04` - Reboot device
- `*** 99` - Factory reset

---

## Configuration File Template

See `HT813_config_template.txt` for a structured template to fill in your specific values.

---

## Need Help?

If you need assistance with any specific values or settings, please provide:
1. Your SIP provider name (or server details)
2. Your country/region (affects FXO impedance, caller ID, etc.)
3. Your call routing preference
4. Your phone number(s)
5. Any specific features you need (fax, call forwarding, etc.)

I'll help you fill in the exact configuration values!
