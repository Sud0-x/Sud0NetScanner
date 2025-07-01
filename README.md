# Sud0NetScanner - Advanced Network Port Scanner

🔥 **A sophisticated and powerful network reconnaissance tool built by Sud0-x**

Sud0NetScanner is a next-generation Python-based network scanning utility that delivers exceptional performance and accuracy. Engineered for cybersecurity professionals, penetration testers, and network administrators who demand precision and speed in their reconnaissance activities.

## 🚀 Features

- **High-Speed Scanning**: Multi-threaded scanning with configurable thread count
- **Service Detection**: Identifies services running on open ports with banner grabbing
- **OS Detection**: Basic operating system fingerprinting using TTL analysis
- **Flexible Target Input**: Supports single IPs, IP ranges, CIDR notation, and hostnames
- **Stealth Mode**: SYN scanning capabilities for stealthy reconnaissance
- **Progress Tracking**: Real-time progress indicator with scan rate statistics
- **Multiple Output Formats**: Console output and JSON export
- **Error Handling**: Robust error handling and graceful interruption
- **Colorized Output**: Beautiful, colored terminal output for better readability

## 📋 Requirements

- Python 3.6 or higher
- Standard Python libraries (no additional packages required)
- Linux/Unix environment (tested on Kali Linux)

## 🛠️ Installation

### Method 1: Clone Repository
```bash
git clone https://github.com/Sud0-x/Sud0NetScanner.git
cd Sud0NetScanner
```

### Method 2: Direct Download
```bash
wget https://raw.githubusercontent.com/Sud0-x/Sud0NetScanner/main/netscanner.py
# or
curl -O https://raw.githubusercontent.com/Sud0-x/Sud0NetScanner/main/netscanner.py
```

### Method 3: Auto Installation
```bash
# Download and run the installation script
curl -sSL https://raw.githubusercontent.com/Sud0-x/Sud0NetScanner/main/install.sh | bash
```

2. Make it executable:
```bash
chmod +x netscanner.py
```

3. Run it:
```bash
python3 netscanner.py -h
```

## 🎯 Usage

### Basic Usage

```bash
# Scan specific ports on a single host
python3 netscanner.py -t 192.168.1.1 -p 22,80,443

# Scan a range of ports
python3 netscanner.py -t 192.168.1.1 -p 1-1000

# Scan multiple hosts
python3 netscanner.py -t 192.168.1.1 192.168.1.2 -p 80,443
```

### Advanced Usage

```bash
# Scan entire subnet with high thread count
python3 netscanner.py -t 192.168.1.0/24 -p 1-1000 -T 200

# Scan IP range with verbose output
python3 netscanner.py -t 10.0.0.1-50 -p 22,80,443,8080 -v

# Stealth scan with custom timeout
python3 netscanner.py -t scanme.nmap.org -p 1-65535 -s --timeout 0.5

# Save results to JSON file
python3 netscanner.py -t 192.168.1.0/24 -p 80,443 -o scan_results.json
```

## 🔧 Command Line Options

| Option | Description |
|--------|-------------|
| `-t, --targets` | Target IP(s), hostname(s), or CIDR notation (required) |
| `-p, --ports` | Port range (e.g., 1-1000, 80,443,22) (required) |
| `-T, --threads` | Number of threads (default: 100) |
| `--timeout` | Connection timeout in seconds (default: 1.0) |
| `-v, --verbose` | Enable verbose output |
| `-s, --stealth` | Enable stealth mode (SYN scan) |
| `-o, --output` | Save results to JSON file |
| `-h, --help` | Show help message |

## 📊 Example Output

```
 ███╗   ██╗███████╗████████╗███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
 ████╗  ██║██╔════╝╚══██╔══╝██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
 ██╔██╗ ██║█████╗     ██║   ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
 ██║╚██╗██║██╔══╝     ██║   ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
 ██║ ╚████║███████╗   ██║   ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
 ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝

Advanced Network Port Scanner v2.0
A powerful Python network scanning tool

[INFO] Starting scan on 1 target(s)
[INFO] Scanning 3 port(s)
[INFO] Using 100 threads
[INFO] Timeout: 1.0s

[SCANNING] Progress: 100.0% (3/3) Rate: 15.2 scans/sec

SCAN RESULTS
============================================================

Host: 192.168.1.1
OS Detection: Linux/Unix
PORT     STATE    SERVICE
----------------------------------------
22       open     SSH (SSH-2.0-OpenSSH_8.2p1)
80       open     HTTP
443      open     HTTPS

SCAN SUMMARY
==============================
Hosts scanned: 1
Ports scanned per host: 3
Total open ports found: 3
Scan duration: 0.20 seconds
Scan rate: 15.00 ports/second
```

## 🎛️ Target Formats

NetScanner supports various target input formats:

- **Single IP**: `192.168.1.1`
- **Multiple IPs**: `192.168.1.1 192.168.1.2`
- **IP Range**: `192.168.1.1-50` (scans .1 through .50)
- **CIDR Notation**: `192.168.1.0/24` (scans entire subnet)
- **Hostname**: `scanme.nmap.org`

## 🎯 Port Formats

Flexible port specification:

- **Single Port**: `80`
- **Multiple Ports**: `22,80,443`
- **Port Range**: `1-1000`
- **Mixed**: `22,80,443,8000-8080`

## 🔒 Scan Modes

### TCP Connect Scan (Default)
- Completes the full TCP handshake
- More reliable but more detectable
- Works without special privileges

### Stealth Mode (SYN Scan)
- Uses SYN packets only
- More stealthy and faster
- May require elevated privileges

## 📈 Performance Optimization

- **Threading**: Adjustable thread count for optimal performance
- **Timeout**: Configurable connection timeout
- **Progress Tracking**: Real-time progress monitoring
- **Memory Efficient**: Minimal memory footprint

## 🛡️ Security Features

- **Graceful Interruption**: Clean exit on Ctrl+C
- **Error Handling**: Robust exception handling
- **Input Validation**: Comprehensive input validation
- **Safe Defaults**: Sensible default values

## 📝 Output Formats

### Console Output
- Colorized, formatted output
- Progress indicators
- Detailed scan summaries

### JSON Export
```json
{
  "scan_info": {
    "targets": ["192.168.1.1"],
    "ports": [22, 80, 443],
    "timestamp": "2024-01-15T10:30:00",
    "duration": 0.85
  },
  "results": {
    "192.168.1.1": [
      {
        "port": 22,
        "state": "open",
        "service": "SSH (SSH-2.0-OpenSSH_8.2p1)"
      }
    ]
  }
}
```

## 🔧 Troubleshooting

### Permission Issues
For stealth mode, you may need elevated privileges:
```bash
sudo python3 netscanner.py -t 192.168.1.1 -p 1-1000 -s
```

### Slow Scanning
- Reduce thread count if experiencing connection issues
- Increase timeout for slow networks
- Use smaller port ranges for faster results

### Network Issues
- Ensure target hosts are reachable
- Check firewall settings
- Verify network connectivity

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Disclaimer

This tool is for educational and authorized testing purposes only. Users are responsible for complying with applicable laws and regulations. Unauthorized scanning of networks is illegal and unethical.

## 🔗 Related Tools

- **Nmap**: The original network discovery tool
- **Masscan**: High-speed port scanner
- **Zmap**: Internet-wide network scanner

## 📞 Support

For issues, questions, or contributions:
- Open an issue on GitHub
- Contact the development team
- Check the documentation

---

**Sud0NetScanner** - Advanced network reconnaissance by Sud0-x! 🔥

**Connect with Sud0-x:**
- GitHub: [@Sud0-x](https://github.com/Sud0-x)
- Repository: [Sud0NetScanner](https://github.com/Sud0-x/Sud0NetScanner)

*"Precision. Power. Performance."* ⚡
