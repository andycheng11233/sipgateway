# SIP Gateway Configuration - Grandstream HT813

Complete configuration guide and templates for setting up a Grandstream HT813 Analog Telephone Adapter (ATA) as a home SIP gateway with analog FXO/FXS ports.

## 📚 Documentation

### Quick Start
- **[HT813 Quick Start Guide](HT813_Quick_Start.md)** - Get up and running in 10 minutes

### Complete Guides
- **[HT813 Configuration Guide](HT813_Configuration_Guide.md)** - Comprehensive configuration guide with all settings explained
- **[Configuration Template](HT813_config_template.txt)** - Fill-in-the-blank template for your specific setup
- **[SIP Provider Examples](SIP_Provider_Examples.md)** - Pre-configured examples for popular VoIP providers
- **[Troubleshooting Guide](Troubleshooting_Guide.md)** - Solutions to common problems and issues

## 🔧 What is the HT813?

The Grandstream HT813 is an Analog Telephone Adapter (ATA) that bridges traditional analog phones with modern VoIP/SIP networks:

- **1 FXS Port (PHONE)**: Connect analog phones or fax machines to make calls via SIP/VoIP
- **1 FXO Port (LINE)**: Connect to PSTN (traditional phone line) for incoming calls or backup
- **Dual SIP Accounts**: Support multiple VoIP providers simultaneously
- **T.38 Fax**: Reliable fax over IP support
- **NAT Traversal**: Works seamlessly behind home routers

## 🚀 Getting Started

### New to VoIP?
Start with the **[Quick Start Guide](HT813_Quick_Start.md)** - it will walk you through basic setup in 10 minutes.

### Need Detailed Configuration?
Review the **[Complete Configuration Guide](HT813_Configuration_Guide.md)** for in-depth explanations of every setting.

### Have a Specific Provider?
Check **[SIP Provider Examples](SIP_Provider_Examples.md)** for pre-configured settings for:
- VoIP.ms
- Flowroute
- Twilio
- Vonage
- Callcentric
- 3CX
- Asterisk/FreePBX
- And more...

### Running Into Issues?
Consult the **[Troubleshooting Guide](Troubleshooting_Guide.md)** for solutions to common problems.

## 📋 What You'll Need

Before starting, gather this information:

### From Your SIP/VoIP Provider:
- [ ] SIP Server Address
- [ ] SIP Username/Account ID
- [ ] SIP Password
- [ ] Port Number (usually 5060)
- [ ] Transport Protocol (UDP/TCP/TLS)

### Your Network:
- [ ] Router with available Ethernet port
- [ ] Static IP or DHCP preference

### Your Hardware:
- [ ] HT813 device
- [ ] Analog phone
- [ ] PSTN line (optional, for FXO port)

## 💡 Common Use Cases

### Use Case 1: Replace Landline with VoIP
**Goal**: Use your existing analog phone with a VoIP service to save money

**Setup**:
1. Connect analog phone to HT813 FXS (PHONE) port
2. Configure SIP account from VoIP provider
3. Make calls through internet instead of phone company

**Benefits**: Lower monthly costs, keep familiar analog phone

---

### Use Case 2: VoIP with PSTN Backup
**Goal**: Primary VoIP calling with automatic fallback to PSTN if internet fails

**Setup**:
1. Connect analog phone to FXS port
2. Connect PSTN line to FXO port
3. Configure both SIP and FXO
4. Set failover rules

**Benefits**: Cost savings + reliability

---

### Use Case 3: Bridge PSTN to SIP Network
**Goal**: Route incoming PSTN calls to SIP system (PBX, softphone, etc.)

**Setup**:
1. Connect PSTN line to FXO port
2. Configure FXO to route to SIP account
3. Incoming PSTN calls forward to SIP

**Benefits**: Integrate old phone line with modern VoIP system

---

### Use Case 4: Fax over IP
**Goal**: Send/receive faxes using VoIP

**Setup**:
1. Connect fax machine to FXS port
2. Enable T.38 protocol
3. Configure for fax-optimized settings

**Benefits**: Fax without dedicated phone line

---

## 🔑 Key Configuration Sections

| Section | Purpose | Documentation |
|---------|---------|---------------|
| **Network Settings** | IP address, DNS, QoS | [Configuration Guide](HT813_Configuration_Guide.md#basic-network-settings) |
| **FXS Port (PHONE)** | SIP account, codecs, dial plan | [Configuration Guide](HT813_Configuration_Guide.md#fxs-port-configuration-phone-port) |
| **FXO Port (LINE)** | PSTN line, caller ID, routing | [Configuration Guide](HT813_Configuration_Guide.md#fxo-port-configuration-line-port) |
| **Call Routing** | How calls are routed between ports | [Configuration Guide](HT813_Configuration_Guide.md#call-routing-strategy) |
| **Dial Plans** | Number patterns and routing rules | [Configuration Guide](HT813_Configuration_Guide.md#advanced-dial-plan-examples) |

## 🛠️ Quick Reference

### Access Device
1. Plug in and connect to network
2. From connected phone, dial `***02` to hear IP address
3. Open browser to `http://[IP_ADDRESS]`
4. Login: `admin` / `admin` (change immediately!)

### IVR Commands (dial from connected phone)
- `***` - Enter IVR menu
- `***02` - Hear IP address
- `***03` - Hear MAC address
- `***04` - Reboot device
- `***99` - Factory reset (WARNING: erases all settings)

### Default Ports
- **Web Interface**: 80 (HTTP) / 443 (HTTPS)
- **SIP**: 5060 (UDP/TCP) / 5061 (TLS)
- **RTP**: 5004-5082 (UDP)

## 🆘 Getting Help

### Need Configuration Assistance?

**I can help you configure your specific setup!** Just provide:

1. **SIP Provider** - Name or server details
2. **Country/Region** - For FXO impedance and caller ID settings
3. **Phone Number(s)** - Your assigned numbers
4. **Use Case** - What you want to accomplish
5. **Special Needs** - Fax, call forwarding, etc.

Example: *"I'm using VoIP.ms in the USA. I want to use my analog phone for VoIP calls with my PSTN line as backup. My PSTN number is (555) 123-4567."*

### Found a Problem?

Check the **[Troubleshooting Guide](Troubleshooting_Guide.md)** for:
- Registration issues
- Audio problems (one-way, echo, choppy)
- FXO/PSTN problems
- Network issues
- Dial plan problems
- Fax issues

### Additional Resources

- **Grandstream Support**: https://www.grandstream.com/support
- **Official Manual**: http://www.grandstream.com/support/ht813
- **Community Forum**: https://community.grandstream.com/
- **VoIP Forums**: https://www.voip-info.org/

## 📝 Configuration Template

Use the **[Configuration Template](HT813_config_template.txt)** to document your setup:
- Fill in all your specific values
- Keep it for future reference
- Use it for disaster recovery
- Share with support if needed

## 🔐 Security Best Practices

1. ✅ **Change default password immediately**
2. ✅ **Use strong SIP passwords** (16+ characters)
3. ✅ **Keep firmware updated**
4. ✅ **Limit web interface access to local network**
5. ✅ **Enable TLS if provider supports it**
6. ✅ **Monitor for unusual call activity**
7. ✅ **Back up configuration regularly**

## 📦 What's Included

```
sipgateway/
├── README.md                          # This file - overview and navigation
├── HT813_Quick_Start.md              # 10-minute setup guide
├── HT813_Configuration_Guide.md      # Complete configuration reference
├── HT813_config_template.txt         # Fill-in-the-blank template
├── SIP_Provider_Examples.md          # Provider-specific configurations
└── Troubleshooting_Guide.md          # Problem-solving guide
```

## 🎯 Next Steps

1. **Read** the [Quick Start Guide](HT813_Quick_Start.md)
2. **Gather** your SIP provider credentials
3. **Connect** your hardware
4. **Configure** following the guides
5. **Test** your setup
6. **Customize** dial plans and features as needed

---

## 📄 License

This documentation is provided as-is for educational and configuration purposes.

## 🤝 Contributing

Have additional provider configurations? Found a solution to a problem? Contributions welcome!

---

**Last Updated**: 2026-01-02  
**Version**: 1.0  
**Device**: Grandstream HT813
