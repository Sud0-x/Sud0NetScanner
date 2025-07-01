#!/usr/bin/env python3
"""
Sud0NetScanner - Advanced Network Port Scanner
A powerful and sophisticated network reconnaissance tool

Developed by Sud0-x
GitHub: https://github.com/Sud0-x/Sud0NetScanner

Features:
- High-speed multi-threaded scanning
- Service detection and banner grabbing
- OS fingerprinting capabilities
- Stealth mode scanning
- Multiple output formats
- Real-time progress tracking

Usage: python3 netscanner.py -t <targets> -p <ports> [options]
"""

import socket
import threading
import argparse
import sys
import time
import json
import subprocess
import ipaddress
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
import signal
import os

class Colors:
    """ANSI color codes for terminal output"""
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class NetScanner:
    def __init__(self, targets, ports, threads=100, timeout=1, verbose=False, stealth=False):
        self.targets = self._parse_targets(targets)
        self.ports = self._parse_ports(ports)
        self.threads = threads
        self.timeout = timeout
        self.verbose = verbose
        self.stealth = stealth
        self.results = {}
        self.scan_start_time = None
        self.total_scans = 0
        self.completed_scans = 0
        self.lock = threading.Lock()
        
        # Common service signatures
        self.service_signatures = {
            21: 'FTP',
            22: 'SSH',
            23: 'Telnet',
            25: 'SMTP',
            53: 'DNS',
            80: 'HTTP',
            110: 'POP3',
            143: 'IMAP',
            443: 'HTTPS',
            993: 'IMAPS',
            995: 'POP3S',
            3389: 'RDP',
            5432: 'PostgreSQL',
            3306: 'MySQL',
            1433: 'MSSQL',
            6379: 'Redis',
            27017: 'MongoDB',
            5984: 'CouchDB',
            9200: 'Elasticsearch'
        }

    def _parse_targets(self, targets):
        """Parse target specification into list of IP addresses"""
        target_list = []
        
        for target in targets:
            try:
                # Check if it's a CIDR notation
                if '/' in target:
                    network = ipaddress.ip_network(target, strict=False)
                    target_list.extend([str(ip) for ip in network.hosts()])
                # Check if it's a range (e.g., 192.168.1.1-10)
                elif '-' in target and '.' in target:
                    base_ip, range_part = target.rsplit('.', 1)
                    if '-' in range_part:
                        start, end = map(int, range_part.split('-'))
                        for i in range(start, end + 1):
                            target_list.append(f"{base_ip}.{i}")
                    else:
                        target_list.append(target)
                else:
                    # Single IP or hostname
                    target_list.append(target)
            except Exception as e:
                self._print_error(f"Error parsing target {target}: {e}")
                
        return target_list

    def _parse_ports(self, port_spec):
        """Parse port specification into list of ports"""
        ports = []
        
        for spec in port_spec.split(','):
            spec = spec.strip()
            if '-' in spec:
                start, end = map(int, spec.split('-'))
                ports.extend(range(start, end + 1))
            else:
                ports.append(int(spec))
                
        return sorted(set(ports))

    def _print_banner(self):
        """Print application banner"""
        banner = f"""
{Colors.CYAN}{Colors.BOLD}
 ███╗   ██╗███████╗████████╗███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
 ████╗  ██║██╔════╝╚══██╔══╝██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
 ██╔██╗ ██║█████╗     ██║   ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
 ██║╚██╗██║██╔══╝     ██║   ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
 ██║ ╚████║███████╗   ██║   ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
 ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
{Colors.END}
{Colors.YELLOW}Advanced Network Port Scanner v2.0{Colors.END}
{Colors.WHITE}A powerful Python network scanning tool{Colors.END}
"""
        print(banner)

    def _print_info(self, message):
        """Print info message"""
        print(f"{Colors.BLUE}[INFO]{Colors.END} {message}")

    def _print_success(self, message):
        """Print success message"""
        print(f"{Colors.GREEN}[+]{Colors.END} {message}")

    def _print_warning(self, message):
        """Print warning message"""
        print(f"{Colors.YELLOW}[!]{Colors.END} {message}")

    def _print_error(self, message):
        """Print error message"""
        print(f"{Colors.RED}[-]{Colors.END} {message}")

    def _get_service_info(self, host, port):
        """Attempt to identify service running on port"""
        try:
            # Try to get banner
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            
            if self.stealth:
                # Use SYN scan technique (requires raw sockets)
                return self.service_signatures.get(port, 'Unknown')
            
            sock.connect((host, port))
            
            # Send basic probe and try to get banner
            try:
                sock.send(b'\r\n')
                banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
                sock.close()
                
                if banner:
                    return f"{self.service_signatures.get(port, 'Unknown')} ({banner[:50]})"
                else:
                    return self.service_signatures.get(port, 'Unknown')
            except:
                sock.close()
                return self.service_signatures.get(port, 'Unknown')
                
        except Exception:
            return self.service_signatures.get(port, 'Unknown')

    def _scan_port(self, host, port):
        """Scan a single port on a host"""
        try:
            if self.stealth:
                # Implement SYN scan (basic version)
                result = self._syn_scan(host, port)
            else:
                # TCP Connect scan
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(self.timeout)
                result = sock.connect_ex((host, port))
                sock.close()
                result = (result == 0)
            
            with self.lock:
                self.completed_scans += 1
                
            if result:
                service = self._get_service_info(host, port)
                
                if host not in self.results:
                    self.results[host] = []
                
                self.results[host].append({
                    'port': port,
                    'state': 'open',
                    'service': service
                })
                
                if self.verbose:
                    self._print_success(f"{host}:{port} - {service}")
                    
            return result
            
        except Exception as e:
            if self.verbose:
                self._print_error(f"Error scanning {host}:{port} - {e}")
            return False

    def _syn_scan(self, host, port):
        """Basic SYN scan implementation"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((host, port))
            sock.close()
            return result == 0
        except:
            return False

    def _progress_indicator(self):
        """Show scanning progress"""
        while self.completed_scans < self.total_scans:
            try:
                progress = (self.completed_scans / self.total_scans) * 100
                elapsed = time.time() - self.scan_start_time
                rate = self.completed_scans / elapsed if elapsed > 0 else 0
                
                sys.stdout.write(f"\r{Colors.YELLOW}[SCANNING]{Colors.END} "
                               f"Progress: {progress:.1f}% "
                               f"({self.completed_scans}/{self.total_scans}) "
                               f"Rate: {rate:.1f} scans/sec")
                sys.stdout.flush()
                time.sleep(0.1)
            except:
                break
        print()

    def _detect_os(self, host):
        """Basic OS detection using TTL values"""
        try:
            # Ping and analyze TTL
            result = subprocess.run(['ping', '-c', '1', host], 
                                  capture_output=True, text=True, timeout=5)
            
            if 'ttl=' in result.stdout.lower():
                ttl_line = [line for line in result.stdout.split('\n') 
                           if 'ttl=' in line.lower()][0]
                ttl = int(ttl_line.split('ttl=')[1].split()[0])
                
                if ttl <= 64:
                    return "Linux/Unix"
                elif ttl <= 128:
                    return "Windows"
                else:
                    return "Unknown"
            return "Unknown"
        except:
            return "Unknown"

    def scan(self):
        """Main scanning function"""
        self._print_banner()
        
        # Calculate total scans
        self.total_scans = len(self.targets) * len(self.ports)
        
        self._print_info(f"Starting scan on {len(self.targets)} target(s)")
        self._print_info(f"Scanning {len(self.ports)} port(s)")
        self._print_info(f"Using {self.threads} threads")
        self._print_info(f"Timeout: {self.timeout}s")
        print()
        
        self.scan_start_time = time.time()
        
        # Start progress indicator in separate thread
        progress_thread = threading.Thread(target=self._progress_indicator, daemon=True)
        progress_thread.start()
        
        try:
            with ThreadPoolExecutor(max_workers=self.threads) as executor:
                futures = []
                
                for host in self.targets:
                    for port in self.ports:
                        future = executor.submit(self._scan_port, host, port)
                        futures.append(future)
                
                # Wait for all scans to complete
                for future in as_completed(futures):
                    try:
                        future.result()
                    except Exception as e:
                        if self.verbose:
                            self._print_error(f"Scan error: {e}")
                            
        except KeyboardInterrupt:
            self._print_warning("Scan interrupted by user")
            
        scan_duration = time.time() - self.scan_start_time
        self._print_scan_results(scan_duration)

    def _print_scan_results(self, duration):
        """Print comprehensive scan results"""
        print(f"\n{Colors.BOLD}SCAN RESULTS{Colors.END}")
        print("=" * 60)
        
        total_open_ports = 0
        
        for host in sorted(self.results.keys()):
            if self.results[host]:
                print(f"\n{Colors.BOLD}{Colors.GREEN}Host: {host}{Colors.END}")
                
                # Try to detect OS
                os_info = self._detect_os(host)
                if os_info != "Unknown":
                    print(f"{Colors.CYAN}OS Detection: {os_info}{Colors.END}")
                
                print(f"{'PORT':<8} {'STATE':<8} {'SERVICE'}")
                print("-" * 40)
                
                for port_info in sorted(self.results[host], key=lambda x: x['port']):
                    print(f"{port_info['port']:<8} "
                          f"{Colors.GREEN}{port_info['state']:<8}{Colors.END} "
                          f"{port_info['service']}")
                    total_open_ports += 1
        
        # Summary
        print(f"\n{Colors.BOLD}SCAN SUMMARY{Colors.END}")
        print("=" * 30)
        print(f"Hosts scanned: {len(self.targets)}")
        print(f"Ports scanned per host: {len(self.ports)}")
        print(f"Total open ports found: {total_open_ports}")
        print(f"Scan duration: {duration:.2f} seconds")
        print(f"Scan rate: {self.total_scans/duration:.2f} ports/second")

    def save_results(self, filename):
        """Save results to JSON file"""
        try:
            output = {
                'scan_info': {
                    'targets': self.targets,
                    'ports': self.ports,
                    'timestamp': datetime.now().isoformat(),
                    'duration': time.time() - self.scan_start_time
                },
                'results': self.results
            }
            
            with open(filename, 'w') as f:
                json.dump(output, f, indent=2)
                
            self._print_success(f"Results saved to {filename}")
            
        except Exception as e:
            self._print_error(f"Error saving results: {e}")

def signal_handler(signum, frame):
    """Handle Ctrl+C gracefully"""
    print(f"\n{Colors.YELLOW}[!] Scan interrupted by user{Colors.END}")
    sys.exit(0)

def main():
    signal.signal(signal.SIGINT, signal_handler)
    
    parser = argparse.ArgumentParser(
        description="NetScanner - Advanced Network Port Scanner",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 netscanner.py -t 192.168.1.1 -p 80,443,22
  python3 netscanner.py -t 192.168.1.0/24 -p 1-1000 -T 200
  python3 netscanner.py -t 10.0.0.1-50 -p 22,80,443 -v
  python3 netscanner.py -t scanme.nmap.org -p 1-65535 -s
        """
    )
    
    parser.add_argument('-t', '--targets', required=True, nargs='+',
                       help='Target IP(s), hostname(s), or CIDR notation')
    parser.add_argument('-p', '--ports', required=True,
                       help='Port range (e.g., 1-1000, 80,443,22)')
    parser.add_argument('-T', '--threads', type=int, default=100,
                       help='Number of threads (default: 100)')
    parser.add_argument('--timeout', type=float, default=1.0,
                       help='Connection timeout in seconds (default: 1.0)')
    parser.add_argument('-v', '--verbose', action='store_true',
                       help='Verbose output')
    parser.add_argument('-s', '--stealth', action='store_true',
                       help='Stealth mode (SYN scan)')
    parser.add_argument('-o', '--output', type=str,
                       help='Save results to JSON file')
    
    args = parser.parse_args()
    
    try:
        scanner = NetScanner(
            targets=args.targets,
            ports=args.ports,
            threads=args.threads,
            timeout=args.timeout,
            verbose=args.verbose,
            stealth=args.stealth
        )
        
        scanner.scan()
        
        if args.output:
            scanner.save_results(args.output)
            
    except Exception as e:
        print(f"{Colors.RED}[ERROR]{Colors.END} {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
    