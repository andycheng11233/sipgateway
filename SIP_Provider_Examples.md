# Common SIP Providers Configuration Examples

This document provides pre-configured examples for popular SIP/VoIP providers to help you quickly set up your HT813.

---

## Table of Contents

1. [VoIP.ms](#voipms)
2. [Flowroute](#flowroute)
3. [Twilio](#twilio)
4. [Vonage (Nexmo)](#vonage-nexmo)
5. [Bandwidth](#bandwidth)
6. [Callcentric](#callcentric)
7. [Google Voice (via OBi)](#google-voice)
8. [3CX](#3cx)
9. [Asterisk/FreePBX](#asteriskfreepbx)
10. [Generic SIP Provider](#generic-sip-provider)

---

## VoIP.ms

**Website**: https://voip.ms

### Configuration
| Parameter | Value |
|-----------|-------|
| Primary SIP Server | `[your_server].voip.ms` (e.g., seattle.voip.ms) |
| Failover SIP Server | Leave blank or use backup server |
| Outbound Proxy | Leave blank |
| SIP User ID | Your VoIP.ms sub-account (e.g., 123456_yoursubaccount) |
| Authenticate ID | Same as SIP User ID |
| Authenticate Password | Your sub-account password |
| Name | Your caller ID name |
| SIP Transport | UDP |
| SIP Port | 5060 |
| NAT Traversal | Keep-Alive |
| STUN Server | stun.voip.ms |

### Notes
- You must create a sub-account in VoIP.ms portal
- Use the server closest to your location for best quality
- Enable SMS to email notification in VoIP.ms portal if desired

### Dial Plan
```
{ x+ | \+x+ | *x+ | 011xx. }
```

---

## Flowroute

**Website**: https://flowroute.com

### Configuration
| Parameter | Value |
|-----------|-------|
| Primary SIP Server | `[your-region].sip.flowroute.com` (e.g., us-west-or.sip.flowroute.com) |
| Failover SIP Server | Leave blank |
| Outbound Proxy | Leave blank |
| SIP User ID | Your Flowroute Access Key |
| Authenticate ID | Your Flowroute Access Key |
| Authenticate Password | Your Flowroute Secret Key |
| Name | Your caller ID name |
| SIP Transport | UDP or TCP |
| SIP Port | 5060 |
| NAT Traversal | Keep-Alive |

### Notes
- Get Access Key and Secret Key from Flowroute portal under "Preferences" → "API Control"
- Flowroute requires you to enable specific phone numbers for inbound calls
- Use region-specific SIP server for lower latency

### Dial Plan
```
{ x+ | \+x+ | 1xxxxxxxxxx | 011xx. }
```

---

## Twilio

**Website**: https://twilio.com

### Configuration
| Parameter | Value |
|-----------|-------|
| Primary SIP Server | `[your-subdomain].pstn.twilio.com` |
| Failover SIP Server | Leave blank |
| Outbound Proxy | Leave blank |
| SIP User ID | Your Twilio SIP username |
| Authenticate ID | Your Twilio SIP username |
| Authenticate Password | Your Twilio SIP password |
| Name | Your caller ID name |
| SIP Transport | UDP |
| SIP Port | 5060 |
| NAT Traversal | Keep-Alive |

### Notes
- You need to create a SIP Domain in Twilio Console
- Set up Voice URLs for handling inbound/outbound calls
- Twilio Elastic SIP Trunking is recommended for better control
- May require TwiML apps for call routing

### Dial Plan
```
{ x+ | \+x+ | 1xxxxxxxxxx }
```

---

## Vonage (Nexmo)

**Website**: https://vonage.com

### Configuration
| Parameter | Value |
|-----------|-------|
| Primary SIP Server | `sip.nexmo.com` |
| Failover SIP Server | Leave blank |
| Outbound Proxy | Leave blank |
| SIP User ID | Your Vonage API Key |
| Authenticate ID | Your Vonage API Key |
| Authenticate Password | Your Vonage API Secret |
| Name | Your caller ID name |
| SIP Transport | UDP or TLS (port 5061) |
| SIP Port | 5060 (UDP) or 5061 (TLS) |
| NAT Traversal | Keep-Alive |

### Notes
- Create SIP credentials in Vonage Dashboard
- Configure voice applications for routing
- TLS recommended for security

---

## Bandwidth

**Website**: https://bandwidth.com

### Configuration
| Parameter | Value |
|-----------|-------|
| Primary SIP Server | `sip.bandwidth.com` |
| Failover SIP Server | Leave blank |
| Outbound Proxy | Leave blank |
| SIP User ID | Your Bandwidth SIP username |
| Authenticate ID | Your Bandwidth SIP username |
| Authenticate Password | Your Bandwidth SIP password |
| Name | Your caller ID name |
| SIP Transport | UDP |
| SIP Port | 5060 |
| NAT Traversal | Keep-Alive |

### Notes
- Create SIP credentials in Bandwidth dashboard
- Configure locations and endpoints
- Supports E911

---

## Callcentric

**Website**: https://callcentric.com

### Configuration
| Parameter | Value |
|-----------|-------|
| Primary SIP Server | `callcentric.com` |
| Failover SIP Server | Leave blank |
| Outbound Proxy | Leave blank |
| SIP User ID | Your 10-digit Callcentric number (17771234567) |
| Authenticate ID | Your 10-digit Callcentric number |
| Authenticate Password | Your extension password |
| Name | Your caller ID name |
| SIP Transport | UDP |
| SIP Port | 5060 |
| NAT Traversal | Keep-Alive |
| STUN Server | stun.callcentric.com |

### Notes
- Use your full 10-digit Callcentric number as username
- Set extension password in Callcentric portal
- Free incoming calls

### Dial Plan
```
{ x+ | \+x+ | 1xxxxxxxxxx | 011xx. | *xx }
```

---

## Google Voice

**Note**: Google Voice doesn't provide direct SIP support. You need an OBi device or use a gateway service.

### Option 1: Using OBiTALK Bridge (Recommended)

**Website**: https://obihai.com

1. Create account at OBiTALK.com
2. Link Google Voice account
3. Configure HT813 to connect to OBiTALK SIP proxy:

| Parameter | Value |
|-----------|-------|
| Primary SIP Server | `ob.obihai.com` |
| SIP User ID | Your OBiTALK username |
| Authenticate Password | Your OBiTALK password |
| SIP Transport | UDP |
| NAT Traversal | Keep-Alive |

### Option 2: Using Simonics Gateway

**Website**: https://simonics.com/gw

Similar setup but requires registration at Simonics.

---

## 3CX

**Website**: https://3cx.com

### Configuration (for 3CX PBX)
| Parameter | Value |
|-----------|-------|
| Primary SIP Server | Your 3CX server IP or FQDN |
| Failover SIP Server | Leave blank |
| Outbound Proxy | Leave blank |
| SIP User ID | Extension number (e.g., 100) |
| Authenticate ID | Extension number |
| Authenticate Password | Extension password |
| Name | User's name |
| SIP Transport | UDP (or as configured in 3CX) |
| SIP Port | 5060 |
| NAT Traversal | Keep-Alive or STUN |

### Notes
- Create extension in 3CX Management Console
- Check "External IP" configuration if 3CX is remote
- May need port forwarding if 3CX is behind NAT
- Support for T.38 fax

### Dial Plan
```
{ x+ | 0xx. | 9[2-9]xxxxxxxxx }
```
(Adjust based on your 3CX dial plan)

---

## Asterisk/FreePBX

**Website**: https://freepbx.org

### Configuration
| Parameter | Value |
|-----------|-------|
| Primary SIP Server | Your Asterisk/FreePBX server IP or hostname |
| Failover SIP Server | Leave blank |
| Outbound Proxy | Leave blank |
| SIP User ID | Extension number (e.g., 1001) |
| Authenticate ID | Extension number |
| Authenticate Password | Extension secret/password |
| Name | Extension name |
| SIP Transport | UDP (chan_sip) or TCP (chan_pjsip) |
| SIP Port | 5060 (chan_sip) or 5060 (chan_pjsip) |
| NAT Traversal | Keep-Alive |

### Asterisk Configuration Example

In your Asterisk `sip.conf` (chan_sip):
```ini
[1001]
type=friend
secret=yourpassword
host=dynamic
context=from-internal
dtmfmode=rfc2833
disallow=all
allow=ulaw
allow=alaw
nat=yes
qualify=yes
```

Or in `pjsip.conf` (chan_pjsip):
```ini
[1001](endpoint-basic)
auth=1001
aors=1001

[1001](auth-userpass)
password=yourpassword
username=1001

[1001](aor-single-reg)
contact=sip:1001@[ht813-ip]:5060
```

### Notes
- Create extension in FreePBX GUI or Asterisk config
- Ensure firewall allows SIP and RTP ports
- Configure NAT settings in Asterisk if needed
- Check Asterisk CLI: `sip show peers` or `pjsip show endpoints`

---

## Generic SIP Provider

If your provider isn't listed, use this template:

### Questions to Ask Your SIP Provider

1. **SIP Server Address** - What is the SIP server hostname or IP?
2. **Authentication** - What are my SIP username and password?
3. **Transport Protocol** - UDP, TCP, or TLS?
4. **Port Number** - What SIP port should I use? (usually 5060)
5. **Registration Required** - Do I need to register? (usually yes)
6. **Proxy Server** - Is an outbound proxy required?
7. **STUN Server** - What STUN server should I use for NAT?
8. **Codec Support** - Which codecs does your service support?
9. **DTMF Method** - RFC2833, SIP INFO, or in-band?
10. **Special Dial Plans** - Any specific dial plan requirements?

### Generic Configuration Template
| Parameter | Your Value |
|-----------|-----------|
| Primary SIP Server | _________________ |
| Outbound Proxy | _________________ |
| SIP User ID | _________________ |
| Authenticate ID | _________________ |
| Authenticate Password | _________________ |
| Name | _________________ |
| SIP Transport | UDP / TCP / TLS |
| SIP Port | _____ |
| NAT Traversal | Keep-Alive / STUN |
| STUN Server | _________________ |

---

## Codec Recommendations by Provider Type

### VoIP Provider (Internet-based)
- **Preferred**: G.711µ (PCMU) or G.711a (PCMA) for best quality
- **Alternative**: G.729 for low bandwidth (requires license)
- **HD Voice**: G.722 if supported by provider

### Local PBX (LAN)
- **Preferred**: G.711µ (PCMU) or G.711a (PCMA)
- **HD Voice**: G.722 for HD audio

### Low Bandwidth Connection
- **Preferred**: G.729 (8 kbps, requires license)
- **Alternative**: G.726 if supported

---

## Testing Your Configuration

After configuring for your provider:

1. **Check Registration Status**
   - Go to: Status → Account Status
   - Look for "Registered" status

2. **Test Call**
   - Pick up analog phone
   - Listen for dial tone
   - Dial a test number

3. **Test Audio Quality**
   - Make a test call
   - Verify both directions
   - Check for echo or delay

4. **Monitor SIP Messages**
   - In HT813 web interface: Status → SIP Messages
   - Look for successful REGISTER and INVITE messages

---

## Need Help with Your Provider?

If your SIP provider isn't listed here, provide me with:

1. Provider name
2. Any documentation or setup guides they provided
3. SIP server address if known
4. Whether you have your credentials

I'll help you create a custom configuration!

---

**Document Version**: 1.0  
**Last Updated**: 2026-01-02
