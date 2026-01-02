# HT813 Troubleshooting Guide

## Common Issues and Solutions

This guide covers the most common problems you might encounter when setting up or using your Grandstream HT813 SIP gateway.

---

## Table of Contents

1. [Registration Issues](#registration-issues)
2. [Audio Problems](#audio-problems)
3. [FXO Port Issues](#fxo-port-issues)
4. [Network Problems](#network-problems)
5. [Dial Plan Issues](#dial-plan-issues)
6. [Fax Problems](#fax-problems)
7. [Hardware Issues](#hardware-issues)
8. [Security and Access](#security-and-access)

---

## Registration Issues

### Problem: SIP Account Won't Register

**Symptoms:**
- Status page shows "Registration Failed"
- No dial tone on analog phone
- "Service Unavailable" message

**Solutions:**

1. **Verify Credentials**
   - Double-check SIP User ID
   - Verify password (case-sensitive)
   - Ensure Authenticate ID is correct
   - Check for extra spaces in fields

2. **Check SIP Server**
   - Ping the SIP server: `ping sip.provider.com`
   - Verify server address is correct
   - Try IP address instead of hostname
   - Check if server is online (provider status page)

3. **Review NAT Settings**
   - Change NAT Traversal to "STUN"
   - Add STUN server: `stun.l.google.com`
   - Enable Keep-Alive packets
   - Increase Keep-Alive interval to 30 seconds

4. **Check Network**
   - Verify internet connection is working
   - Test from another SIP device if available
   - Check router firewall isn't blocking SIP (port 5060)
   - Disable SIP ALG in router settings

5. **SIP Transport**
   - Try changing from UDP to TCP
   - If using TLS, verify port 5061 is open
   - Check if provider requires specific transport

6. **Provider-Specific**
   - Check account status with provider
   - Verify account is active and paid
   - Check for IP restrictions on account
   - Review provider's firewall whitelist requirements

### Problem: Registration Keeps Dropping

**Symptoms:**
- Intermittent "Service Unavailable"
- Must reboot device to restore service
- Registration works but fails after time

**Solutions:**

1. **Adjust Timers**
   - Increase Registration Expiration to 300-3600 seconds
   - Enable Session Timer
   - Set Keep-Alive interval to 20-30 seconds

2. **Network Stability**
   - Check for packet loss: `ping -c 100 8.8.8.8`
   - Monitor router logs for disconnections
   - Test with wired connection instead of WiFi
   - Update router firmware

3. **NAT Issues**
   - Enable "Symmetric RTP"
   - Use STUN server
   - Set up static port forwarding in router
   - Consider setting static IP for HT813

---

## Audio Problems

### Problem: One-Way Audio (Can Hear But Can't Be Heard)

**Symptoms:**
- You can hear the other party
- They cannot hear you
- Or vice versa

**Solutions:**

1. **Enable STUN**
   - Go to FXS Port settings
   - Set NAT Traversal to "STUN"
   - Add STUN Server: `stun.l.google.com`
   - Save and reboot

2. **Port Forwarding**
   - Forward UDP ports 5004-5082 to HT813 IP
   - Forward UDP port 5060 to HT813 IP
   - Set HT813 to static IP in router
   - Reboot router after changes

3. **Symmetric RTP**
   - Enable "Symmetric RTP" in SIP settings
   - Enable "Support SIP Instance ID"
   - Save and test

4. **Firewall**
   - Check router firewall settings
   - Temporarily disable firewall to test
   - Add exception for HT813 IP
   - Disable SIP ALG in router

### Problem: No Audio at All (Dead Air)

**Symptoms:**
- Call connects but silence
- No audio in either direction

**Solutions:**

1. **Codec Mismatch**
   - Check supported codecs in account settings
   - Enable common codecs: PCMU, PCMA
   - Disable uncommon codecs: iLBC, Speex
   - Match codec settings to provider requirements

2. **RTP Issues**
   - Change Local RTP Port (try 10000-10100)
   - Disable "Use Random Port"
   - Check router isn't blocking RTP ports
   - Enable "Symmetric RTP"

3. **DTMF Settings**
   - Set DTMF to RFC2833
   - If that fails, try "In Audio"
   - Match provider requirements

### Problem: Echo on Calls

**Symptoms:**
- Hear your own voice with delay
- Other party complains about echo

**Solutions:**

1. **Echo Cancellation**
   - Verify Echo Cancellation is enabled
   - Increase Echo Canceller tail length
   - Try different echo cancellation settings

2. **Audio Levels**
   - Reduce RX Gain (try -3dB)
   - Reduce TX Gain (try -3dB)
   - Adjust gradually to find sweet spot

3. **Impedance**
   - Verify impedance matches your country
   - USA/Canada: 600 ohm
   - Europe: 900 ohm
   - UK/Australia: Complex 2

4. **Network**
   - Check for high latency: `ping sip.provider.com`
   - Look for packet loss
   - Use QoS to prioritize voice traffic

### Problem: Choppy or Robotic Audio

**Symptoms:**
- Audio cuts in and out
- Robotic or metallic sound
- Words missing

**Solutions:**

1. **Network Quality**
   - Test bandwidth: speedtest.net
   - Check for packet loss
   - Verify at least 100 kbps available per call
   - Use QoS on router

2. **Jitter Buffer**
   - Change to "Adaptive" jitter buffer
   - Increase jitter buffer size
   - Try "Fixed" buffer if adaptive doesn't help

3. **Codec Selection**
   - Try different codec (G.711 preferred)
   - Disable G.729 if bandwidth allows
   - Enable "Use First Matching Vocoder"

4. **Network Issues**
   - Disable other heavy bandwidth usage
   - Check for network congestion
   - Try different time of day

### Problem: Volume Too Low or Too High

**Symptoms:**
- Can barely hear other party
- Volume too loud causing distortion

**Solutions:**

1. **Adjust Gain Settings**
   - RX Gain: Affects what you hear (0 to +6dB)
   - TX Gain: Affects what they hear (0 to +6dB)
   - Start with 0dB and adjust in 1dB increments
   - Don't exceed +6dB (causes distortion)

2. **Phone Settings**
   - Check volume on analog phone itself
   - Some phones have volume controls
   - Try different analog phone

---

## FXO Port Issues

### Problem: FXO Port Not Detecting PSTN Line

**Symptoms:**
- No incoming calls from PSTN
- FXO status shows "Not Connected"
- Can't make calls through PSTN

**Solutions:**

1. **Physical Connection**
   - Verify cable connected to LINE port (not PHONE)
   - Check cable is working (test with regular phone)
   - Ensure wall jack is active
   - Try different phone cable

2. **Impedance Settings**
   - Set impedance to match your country:
     - USA/Canada: 600 ohm
     - Europe: 900 ohm
     - UK/Australia: Complex 2
   - Wrong impedance prevents detection

3. **Voltage Threshold**
   - Adjust "Voltage Threshold" if line is weak
   - Lower for weaker PSTN lines
   - Check with voltmeter (should be 48V DC)

4. **Line Type**
   - Ensure it's a standard analog line
   - Won't work with digital PBX lines
   - Won't work with VoIP ATA output
   - Must be true PSTN or analog PBX port

### Problem: Caller ID Not Working on FXO

**Symptoms:**
- Calls come through but no caller ID
- Shows "Unknown" or no number

**Solutions:**

1. **Caller ID Settings**
   - Set Caller ID Scheme to match country:
     - USA: Bellcore/Telcordia
     - Europe: ETSI
     - UK: BT
   - Wrong scheme prevents caller ID detection

2. **Caller ID Type**
   - Try DTMF first (USA standard)
   - If not working, try FSK
   - May need both enabled

3. **Service Subscription**
   - Verify caller ID is activated with phone company
   - May be separate service
   - Test with regular phone first

4. **Timing**
   - Increase "Delay Before Answer" to allow time for CID
   - Set to 2000-4000ms
   - Caller ID comes between first and second ring

### Problem: Calls Disconnect Prematurely on FXO

**Symptoms:**
- PSTN calls drop after few seconds
- Random disconnections
- Works sometimes, not others

**Solutions:**

1. **Loop Current Detection**
   - Enable "Loop Current Disconnect Detection"
   - Adjust sensitivity if available
   - May need to disable if line is unusual

2. **Disconnect Tone Detection**
   - Enable "Disconnect Tone Detection"
   - Adjust tone frequency if customizable
   - Test with different settings

3. **Polarity Reversal**
   - Enable "Polarity Reversal Detection" if available
   - Some phone systems use this to signal disconnect
   - May need to disable on others

---

## Network Problems

### Problem: Can't Access Web Interface

**Symptoms:**
- Browser shows "Cannot connect"
- Timeout errors
- Can't reach device

**Solutions:**

1. **Verify IP Address**
   - Dial ***02 from analog phone
   - Check router DHCP client list
   - Try both HTTP and HTTPS
   - Try different browser

2. **Network Connection**
   - Check Ethernet cable is connected
   - Look at LED lights on device
   - Verify device is powered on
   - Try different Ethernet cable

3. **Firewall/Security**
   - Temporarily disable computer firewall
   - Try from different computer
   - Check if router blocks access between clients
   - Verify you're on same network/subnet

4. **Factory Reset**
   - As last resort: dial ***99 from phone
   - Wait for device to reboot
   - Try default IP: 192.168.1.1 or use DHCP IP

### Problem: Device Not Getting IP Address

**Symptoms:**
- No IP announced via IVR
- Not showing in router DHCP list
- Can't connect to network

**Solutions:**

1. **DHCP Settings**
   - Verify router DHCP is enabled
   - Check DHCP pool has available addresses
   - Reboot router
   - Try static IP configuration

2. **Network Cable**
   - Try different Ethernet cable
   - Check cable is Cat5e or better
   - Verify router port is working
   - Look for link lights

3. **Factory Reset**
   - Reset device: ***99
   - Try after fresh boot
   - Check router logs for errors

---

## Dial Plan Issues

### Problem: Can't Dial Certain Numbers

**Symptoms:**
- Some numbers work, others don't
- Fast busy signal
- Numbers not accepted

**Solutions:**

1. **Check Dial Plan**
   - Review current dial plan syntax
   - Ensure pattern matches numbers you need
   - Use: `{ x+ }` for maximum flexibility
   - Add specific patterns as needed

2. **Common Dial Plans**
   
   For USA (permissive):
   ```
   { x+ | \+x+ | *x+ | 011xx. }
   ```
   
   For USA (restrictive):
   ```
   { [2-9]11 | 1[2-9]xxxxxxxxx | [2-9]xxxxxxxxx }
   ```
   
   For International:
   ```
   { x+ | \+x+ | 00xx. | 011xx. }
   ```

3. **Test Pattern**
   - Simplify to `{ x+ }` for testing
   - If works, dial plan was too restrictive
   - Gradually add restrictions back

### Problem: Delay Before Call Connects

**Symptoms:**
- Must wait after dialing
- Long pause before calling
- Need to press additional key

**Solutions:**

1. **Interdigit Timeout**
   - Reduce "Interdigit Long Timeout" (try 3 seconds)
   - Reduce "Interdigit Short Timeout" (try 1 second)
   - Or add terminating digit to dial plan

2. **Dial Plan Terminator**
   - Add `#` as call terminator
   - Change dial plan to: `{ x+# }`
   - User dials number then presses #
   - Immediate calling, no timeout wait

3. **No Answer Timeout**
   - Adjust "No Answer Timeout"
   - Set to appropriate time for your use

---

## Fax Problems

### Problem: Fax Fails or Poor Quality

**Symptoms:**
- Fax won't send/receive
- Partial pages
- Garbled output

**Solutions:**

1. **Use T.38**
   - Enable T.38 Fax support
   - Set Fax Mode to "T.38"
   - Verify provider supports T.38
   - Enable T.38 redundancy

2. **Disable VAD**
   - Voice Activity Detection interferes with fax
   - Disable VAD for fax account
   - Disable Echo Cancellation

3. **Codec Selection**
   - Use G.711 (PCMU or PCMA) only
   - Disable all other codecs for fax
   - Compressed codecs (G.729) break fax

4. **Jitter Buffer**
   - Use Fixed jitter buffer
   - Set to medium or high
   - Disable jitter buffer adaptation

5. **Use PSTN Instead**
   - If VoIP fax unreliable, use FXO port
   - Connect fax to PSTN line
   - More reliable for important faxes

---

## Hardware Issues

### Problem: Device Keeps Rebooting

**Symptoms:**
- Random reboots
- Loses registration frequently
- Unstable operation

**Solutions:**

1. **Power Supply**
   - Use official Grandstream power adapter
   - Check voltage is correct
   - Try different power outlet
   - Test with different power adapter if available

2. **Firmware**
   - Update to latest firmware
   - Check Grandstream website
   - May fix stability issues
   - Read release notes first

3. **Overheating**
   - Ensure adequate ventilation
   - Don't stack devices on top
   - Keep away from heat sources
   - Check if device is hot to touch

4. **Factory Reset**
   - May have corrupted configuration
   - Reset to factory defaults
   - Reconfigure from scratch

### Problem: No LED Lights

**Symptoms:**
- Device appears dead
- No lights at all

**Solutions:**

1. **Power**
   - Check power adapter is connected
   - Verify outlet has power
   - Try different outlet
   - Check power adapter LED

2. **Hardware Failure**
   - If truly no power, may be defective
   - Contact Grandstream support
   - Check warranty status

---

## Security and Access

### Problem: Forgot Admin Password

**Solutions:**

1. **Factory Reset**
   - Dial ***99 from analog phone
   - This resets to default password "admin"
   - All configuration will be lost
   - Must reconfigure device

2. **Prevention**
   - Document your password securely
   - Use password manager
   - Keep backup of configuration

### Problem: Account Hacked or Toll Fraud

**Symptoms:**
- Unexpected international calls
- High bills from provider
- Unauthorized usage

**Solutions:**

1. **Immediate Actions**
   - Change SIP password immediately
   - Disable account at provider
   - Review call logs
   - Contact provider about fraud

2. **Security Hardening**
   - Use strong SIP password (16+ characters)
   - Enable TLS if provider supports
   - Restrict allowed IPs at provider
   - Disable international calling if not needed
   - Monitor usage regularly

3. **Prevention**
   - Never use default passwords
   - Keep firmware updated
   - Limit web interface access to local network
   - Disable unused accounts
   - Enable fail2ban on provider if available

---

## Getting More Help

### Built-in Diagnostics

1. **SIP Messages**
   - Status → SIP Messages
   - Shows SIP traffic
   - Look for error codes

2. **System Log**
   - Maintenance → System Log
   - Shows device events
   - Look for errors

3. **Network Capture**
   - Maintenance → Packet Capture
   - Capture traffic for analysis
   - Send to support if needed

### SIP Response Codes

Common error codes and meaning:

- **401 Unauthorized** - Wrong username or password
- **403 Forbidden** - Account disabled or IP blocked
- **404 Not Found** - Wrong server address or account doesn't exist
- **408 Request Timeout** - Network issues, can't reach server
- **480 Temporarily Unavailable** - Service down or account issue
- **486 Busy Here** - Called party is busy
- **503 Service Unavailable** - SIP server problem

### Contact Support

**Grandstream Support:**
- Website: https://www.grandstream.com/support
- Documentation: http://www.grandstream.com/support/ht813
- Forum: https://community.grandstream.com/
- Email: support@grandstream.com

**Your SIP Provider:**
- Check their support page
- Often have specific configuration guides
- Can verify account status

**Community Help:**
- VoIP-info.org forums
- Reddit: r/VOIP
- Provide configuration details (hide passwords!)

---

## Preventive Maintenance

### Regular Tasks

1. **Weekly**
   - Check registration status
   - Test call quality
   - Review call logs

2. **Monthly**
   - Check for firmware updates
   - Review system logs
   - Verify backup configuration saved

3. **Quarterly**
   - Change admin password
   - Review security settings
   - Test failover if configured

4. **Backup Configuration**
   - Download config file: Maintenance → Backup
   - Save securely
   - Document any customizations

---

**Document Version**: 1.0  
**Last Updated**: 2026-01-02
