# HT813 Quick Start Guide

## 🚀 Quick Setup in 10 Minutes

This is a simplified quick-start guide to get your HT813 up and running quickly. For detailed configuration options, see [HT813_Configuration_Guide.md](HT813_Configuration_Guide.md).

---

## What You'll Need

- ✅ Grandstream HT813 device
- ✅ Ethernet cable (to connect to your router)
- ✅ Power adapter (included with HT813)
- ✅ Analog phone (to connect to FXS/PHONE port)
- ✅ PSTN line (optional - for FXO/LINE port)
- ✅ SIP account credentials from your VoIP provider

---

## Step-by-Step Setup

### Step 1: Connect Hardware (2 minutes)

```
[Wall Outlet] ←─── Power Adapter ───→ [HT813]
                                         │
[Router] ←─────── Ethernet Cable ─────→ [HT813 LAN Port]
                                         │
[Analog Phone] ←─── Phone Cable ───→ [HT813 PHONE Port]
                                         │
[Wall Phone Jack] ←─ Phone Line ───→ [HT813 LINE Port] (optional)
```

1. **Connect power** - Plug in the power adapter
2. **Connect to network** - Ethernet cable from router to HT813 LAN port
3. **Connect phone** - Your analog phone to the PHONE port (FXS)
4. **Connect PSTN** (optional) - Your phone line to the LINE port (FXO)

Wait 30 seconds for the device to boot up.

---

### Step 2: Find Device IP Address (1 minute)

Pick up the phone connected to the PHONE port and dial:

```
***02
```

Listen to the announced IP address (e.g., "192.168.1.100").

Alternative: Check your router's DHCP client list for "Grandstream" or "HT813".

---

### Step 3: Access Web Interface (1 minute)

1. Open your web browser
2. Go to: `http://[IP_ADDRESS]` (e.g., http://192.168.1.100)
3. Login with:
   - **Username**: `admin`
   - **Password**: `admin`
4. **IMPORTANT**: You'll be prompted to change the password - do this now!

---

### Step 4: Configure SIP Account (4 minutes)

Navigate to: **FXS PORT** tab

Fill in these essential fields with your SIP provider's information:

| Field | Example | Your Value |
|-------|---------|------------|
| **Primary SIP Server** | sip.yourprovider.com | _____________ |
| **SIP User ID** | 1234567890 | _____________ |
| **Authenticate ID** | 1234567890 | _____________ |
| **Authenticate Password** | your_password | _____________ |
| **Name** | Your Name | _____________ |

Set these recommended values:

| Field | Set to |
|-------|--------|
| **Account Active** | Yes |
| **SIP Registration** | Yes |
| **SIP Transport** | UDP |
| **NAT Traversal** | Keep-Alive |

Scroll down to **Dial Plan** and enter:
```
{ x+ | \+x+ | *x+ }
```

---

### Step 5: Configure FXO Port (1 minute) - Optional

If you connected a PSTN line to the LINE port:

Navigate to: **FXO PORT** tab

| Field | Set to |
|-------|--------|
| **Enable FXO** | Yes |
| **Impedance** | 600 ohm (USA/Canada) or match your country |
| **Caller ID Scheme** | Bellcore/Telcordia (USA) or match your country |
| **Loop Current Disconnect** | Yes |

---

### Step 6: Save and Reboot (1 minute)

1. Click **Save** at the bottom of the page
2. Click **Apply** when prompted
3. Wait for the device to reboot (about 30 seconds)

---

### Step 7: Test Your Setup (2 minutes)

#### Test FXS Port (VoIP):
1. Pick up the analog phone
2. You should hear a dial tone
3. Dial a test number
4. If the call goes through, FXS is working! ✅

#### Test FXO Port (PSTN):
1. Call your PSTN line from another phone
2. The call should come through
3. Answer it to verify audio quality ✅

---

## Common Issues & Quick Fixes

### ❌ No dial tone on analog phone

**Fix**: 
- Check SIP server address
- Verify username and password
- Look at device LEDs - should have solid network light

### ❌ Can't register with SIP provider

**Fix**:
- Double-check all credentials
- Try changing NAT Traversal to "STUN"
- Add STUN server: `stun.l.google.com`

### ❌ One-way audio (can't hear or be heard)

**Fix**:
- Enable STUN (see above)
- In router, forward ports 5004-5082 (UDP) to HT813 IP
- Set HT813 to static IP in your router

### ❌ No web interface access

**Fix**:
- Verify IP address (dial ***02 on phone)
- Try a different browser
- Factory reset: dial ***99 from phone

---

## Next Steps

✅ **You're done with basic setup!**

For advanced features, refer to:
- [Full Configuration Guide](HT813_Configuration_Guide.md) - Detailed settings
- [Configuration Template](HT813_config_template.txt) - Fill-in template for your setup

---

## Need Help?

I can help you with:
- ✅ Filling in specific values for your SIP provider
- ✅ Setting up dial plans for your calling needs
- ✅ Configuring call routing strategies
- ✅ Troubleshooting any issues

Just provide:
1. Your SIP provider name (or server details if known)
2. Your country/region
3. What you want to do with the setup

Example: "I'm using VoIP.ms as my provider in the USA, and I want to use my analog phone to make calls through VoIP with my PSTN line as backup."

---

## Quick Reference

### IVR Codes (dial from analog phone):
- `***` - Enter IVR menu
- `***02` - Hear IP address
- `***03` - Hear MAC address  
- `***04` - Reboot device
- `***99` - Factory reset

### Default Ports:
- Web Interface: 80 (HTTP) / 443 (HTTPS)
- SIP: 5060 (UDP/TCP) / 5061 (TLS)
- RTP: 5004-5082 (UDP)

### LED Indicators:
- **Power** - Solid green = powered on
- **Network** - Blinking = network activity
- **Phone** - Solid = phone off-hook
- **Line** - Solid = PSTN line connected

---

**Document Version**: 1.0  
**Last Updated**: 2026-01-02
