import nmap
import requests
import json
from datetime import datetime
from core.database import SessionLocal, Asset, Vulnerability

class VulnerabilityScanner:
    def __init__(self):
        self.nm = nmap.PortScanner()
        self.session = SessionLocal()
        
    def discover_assets(self, network_range):
        """Discover assets in network range"""
        print(f"[+] Scanning network: {network_range}")
        
        try:
            self.nm.scan(network_range, arguments='-sn')  # Ping scan
            discovered_hosts = []
            
            for host in self.nm.all_hosts():
                if self.nm[host].state() == 'up':
                    hostname = self.nm[host].hostname() or 'Unknown'
                    
                    # Check if asset exists
                    existing_asset = self.session.query(Asset).filter_by(ip_address=host).first()
                    
                    if not existing_asset:
                        asset = Asset(
                            hostname=hostname,
                            ip_address=host,
                            asset_type='unknown',
                            criticality='medium',
                            status='active'
                        )
                        self.session.add(asset)
                        discovered_hosts.append(host)
            
            self.session.commit()
            print(f"[+] Discovered {len(discovered_hosts)} new assets")
            return discovered_hosts
            
        except Exception as e:
            print(f"[-] Asset discovery failed: {e}")
            return []
    
    def port_scan(self, target):
        """Perform port scan on target"""
        try:
            self.nm.scan(target, '1-1000', '-sV')
            return self.nm[target]
        except Exception as e:
            print(f"[-] Port scan failed for {target}: {e}")
            return None
    
    def fetch_cve_data(self, cve_id):
        """Fetch CVE data from NVD"""
        url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?cveId={cve_id}"
        
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(f"[-] Failed to fetch CVE {cve_id}: {e}")
        
        return None