# 🛡️ Vulnerability Management System

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-blue?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.21-blue?style=flat&logo=sqlite&logoColor=white)](https://www.sqlalchemy.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-blue)](https://github.com/Jybhavsar12/vuln-management-system)

**🎯 Enterprise-Grade Vulnerability Management & Asset Discovery Platform**

*Automate vulnerability assessment with military-grade precision*

[🚀 Quick Start](#-quick-start) • [📖 Documentation](#-documentation) • [🛠️ Features](#️-features) • [⚠️ Legal Notice](#️-legal-notice)

</div>

---

## 🔥 Overview

The **Vulnerability Management System** is a comprehensive security platform designed for enterprise vulnerability assessment, asset discovery, and risk management. Built with Python and featuring a cyberpunk-inspired web interface, this system provides automated vulnerability scanning, CVE tracking, and real-time security monitoring.

### 🎭 Key Highlights

- **🔍 Automated Asset Discovery** - Network scanning and inventory management
- **🎯 Vulnerability Assessment** - CVE integration and risk scoring
- **🌐 Real-Time Dashboard** - Monitor security posture in real-time
- **📊 Risk Management** - CVSS-based vulnerability prioritization
- **🔄 API Integration** - RESTful API for automation and integration
- **📈 Reporting Engine** - Comprehensive security reports

---

## 🛠️ Features

### 🎯 Core Capabilities

| Feature | Description | Status |
|---------|-------------|--------|
| **Asset Discovery** | Automated network scanning with nmap | ✅ Active |
| **Vulnerability Database** | CVE tracking and management | ✅ Active |
| **Web Dashboard** | Real-time security monitoring | ✅ Active |
| **REST API** | Programmatic access to all features | ✅ Active |
| **Risk Scoring** | CVSS-based vulnerability assessment | ✅ Active |
| **Database Integration** | SQLite/PostgreSQL support | ✅ Active |

### 🚀 Advanced Features

- **🔄 Auto-Discovery** - Scheduled network scanning
- **🎨 Cyberpunk UI** - Matrix-inspired security dashboard
- **📡 Multi-Protocol Support** - TCP/UDP scanning capabilities
- **🔐 CVE Integration** - National Vulnerability Database (NVD) API
- **📊 Real-Time Updates** - Live vulnerability status monitoring
- **🎭 Enterprise Ready** - Scalable architecture for large networks

---

## 🚀 Quick Start

### ⚡ One-Command Deployment

```bash
# Clone the repository
git clone https://github.com/Jybhavsar12/vuln-management-system.git
cd vuln-management-system

# Deploy everything with one command
chmod +x deploy.sh && ./deploy.sh
```

### 🎯 Launch System

```bash
# Start the vulnerability management system
python3 app.py
```

### 🌐 Access Dashboard

Open your browser to: **http://localhost:5001**

---

## 📁 Project Structure

```
vuln-management-system/
├── 🚀 deploy.sh              # One-click deployment script
├── 🎯 app.py                 # Main application controller
├── 📋 requirements.txt       # Python dependencies
├── 📖 README.md              # This comprehensive documentation
├── ⚙️ setup.py               # Package configuration
├── 
├── 🔍 core/                  # Core System Components
│   ├── __init__.py
│   ├── database.py           # SQLAlchemy models and database
│   └── scanner.py            # Vulnerability scanning engine
├── 
├── 🌐 api/                   # REST API Endpoints
│   ├── __init__.py
│   ├── assets.py             # Asset management API
│   ├── vulnerabilities.py   # Vulnerability management API
│   └── scans.py              # Scanning operations API
├── 
├── 🖥️ web/                   # Web Interface
│   ├── __init__.py
│   └── dashboard.py          # Main security dashboard
├── 
├── 📊 database/              # Database Files
│   └── vuln_management.db    # SQLite database
├── 
├── 📝 logs/                  # System Logs
├── 📄 reports/               # Generated Reports
└── ⚙️ config/                # Configuration Files
```

---

## 🎯 Usage Guide

### 🔍 Asset Discovery

```bash
# Start the system
python3 app.py

# Access web dashboard
# Navigate to: http://localhost:5001

# Use API for programmatic access
curl -X POST http://localhost:5001/api/assets/discover \
  -H "Content-Type: application/json" \
  -d '{"network_range": "192.168.1.0/24"}'
```

### 🎯 Vulnerability Management

```bash
# Search for specific CVE
curl -X POST http://localhost:5001/api/vulnerabilities/search \
  -H "Content-Type: application/json" \
  -d '{"cve_id": "CVE-2023-12345"}'

# Get all vulnerabilities
curl http://localhost:5001/api/vulnerabilities/
```

### 🔍 Security Scanning

```bash
# Start network discovery scan
curl -X POST http://localhost:5001/api/scans/start \
  -H "Content-Type: application/json" \
  -d '{"target": "192.168.1.0/24", "type": "discovery"}'

# Start port scan
curl -X POST http://localhost:5001/api/scans/start \
  -H "Content-Type: application/json" \
  -d '{"target": "192.168.1.100", "type": "port"}'
```

### 🌐 Web Dashboard Features

- **📊 Real-Time Asset Monitoring** - Live inventory updates every 30 seconds
- **🎯 Quick Action Buttons** - Discover assets, start scans, export reports
- **📈 Vulnerability Statistics** - CVE tracking, severity distribution
- **🎨 Cyberpunk Interface** - Matrix-inspired design with green terminal aesthetics
- **📱 Responsive Design** - Works on desktop, tablet, and mobile devices

---

## 🛡️ Security Features

### 🔐 Operational Security

- **🎭 Network Stealth** - Configurable scan intensity and timing
- **🔄 Database Encryption** - Secure storage of sensitive data
- **📊 Audit Logging** - Comprehensive operation tracking
- **🌐 API Security** - JWT-based authentication ready

### 🛠️ Technical Security

- **🔒 Input Validation** - Comprehensive parameter sanitization
- **📝 Error Handling** - Secure error messages and logging
- **🎯 SQL Injection Protection** - SQLAlchemy ORM security
- **⚡ Rate Limiting** - API abuse prevention (ready for implementation)

---

## 🎨 Web Interface Preview

```
🛡️ VULNERABILITY MANAGEMENT SYSTEM
Enterprise Security Dashboard - Port 5001
═══════════════════════════════════════

System Overview
Total Assets: 15        Critical Vulns: 3
Last Scan: 2024-01-15 14:30:25

Asset Discovery
Network Range: [192.168.1.0/24] [Discover Assets]

Asset Inventory
┌─────────────────────────────────────────────────┐
│ DESKTOP-ABC123 - 192.168.1.100                 │
│ OS: Windows 10 21H2 - Criticality: High        │
│ Status: Active - Last Scan: 2024-01-15 14:25   │
└─────────────────────────────────────────────────┘
```

---

## 🔧 Advanced Configuration

### 🎯 Database Configuration

```python
# PostgreSQL (Production)
DATABASE_URL = "postgresql://user:password@localhost/vuln_mgmt"

# SQLite (Development)
DATABASE_URL = "sqlite:///vuln_management.db"
```

### 🌐 API Configuration

```python
# Custom API settings
app.config.update(
    SECRET_KEY='your-secret-key',
    JWT_SECRET_KEY='jwt-secret-key',
    JWT_ACCESS_TOKEN_EXPIRES=timedelta(hours=24),
    DEBUG=False
)
```

### 🔍 Scanner Configuration

```python
# Custom scanning parameters
scanner = VulnerabilityScanner()
scanner.configure(
    scan_timeout=300,
    max_threads=10,
    stealth_mode=True
)
```

---

## 📊 API Documentation

### 🎯 Assets API

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/assets/` | GET | Get all assets |
| `/api/assets/discover` | POST | Discover network assets |
| `/api/assets/<id>` | DELETE | Delete specific asset |

### 🔍 Vulnerabilities API

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/vulnerabilities/` | GET | Get all vulnerabilities |
| `/api/vulnerabilities/search` | POST | Search CVE database |
| `/api/vulnerabilities/<id>` | DELETE | Delete vulnerability |

### 🚀 Scans API

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/scans/start` | POST | Start vulnerability scan |
| `/api/scans/status` | GET | Get scan status |
| `/api/scans/history` | GET | Get scan history |

---

## 🔍 Troubleshooting

### 🚨 Common Issues

| Issue | Solution |
|-------|----------|
| **Port 5000 in use** | System uses port 5001 (macOS AirPlay fix) |
| **Permission denied** | Run `chmod +x deploy.sh` before execution |
| **Import errors** | Install dependencies: `pip3 install -r requirements.txt` |
| **Database locked** | Stop all processes and restart system |
| **Nmap not found** | Install nmap: `sudo apt install nmap` (Linux) or `brew install nmap` (macOS) |

### 🛠️ Debug Mode

```bash
# Enable debug logging
export FLASK_DEBUG=1
python3 app.py

# Test database connection
python3 -c "from core.database import init_db; init_db()"

# Test network connectivity
python3 -c "
from core.scanner import VulnerabilityScanner
scanner = VulnerabilityScanner()
print('Scanner initialized successfully')
"
```

---

## 🎯 Enterprise Deployment

### 🏢 Production Setup

```bash
# 1. Deploy with PostgreSQL
export DATABASE_URL="postgresql://user:pass@localhost/vuln_mgmt"
python3 app.py

# 2. Configure reverse proxy (nginx)
# 3. Set up SSL/TLS certificates
# 4. Configure firewall rules
# 5. Set up monitoring and logging
```

### 🔄 Automation & Integration

```bash
# Scheduled scanning with cron
0 2 * * * cd /path/to/vuln-management-system && python3 -c "
from core.scanner import VulnerabilityScanner
scanner = VulnerabilityScanner()
scanner.discover_assets('10.0.0.0/8')
"

# Integration with SIEM systems
curl -X GET http://localhost:5001/api/vulnerabilities/ | \
  jq '.[] | select(.severity=="critical")' | \
  logger -t vuln-mgmt
```

---

## 🤝 Contributing

We welcome contributions from the cybersecurity community!

### 🎯 How to Contribute

1. **🍴 Fork** the repository
2. **🌿 Create** a feature branch (`git checkout -b feature/awesome-feature`)
3. **💻 Commit** your changes (`git commit -m 'Add awesome feature'`)
4. **🚀 Push** to the branch (`git push origin feature/awesome-feature`)
5. **📝 Open** a Pull Request

### 🛠️ Development Guidelines

- Follow PEP 8 Python style guidelines
- Add comprehensive error handling
- Include detailed docstrings and comments
- Test on multiple platforms
- Update documentation accordingly

---

## 📚 Documentation

### 📖 Additional Resources

- **🎯 [API Reference](docs/api.md)** - Complete API documentation
- **🔍 [Scanner Guide](docs/scanner.md)** - Vulnerability scanning techniques
- **🌐 [Web Interface](docs/web.md)** - Dashboard user guide
- **🛡️ [Security Best Practices](docs/security.md)** - Operational security
- **📊 [Database Schema](docs/database.md)** - Data model documentation

### 🎓 Learning Resources

- **Vulnerability Management** - Industry best practices
- **CVE Database** - Understanding vulnerability data
- **Network Scanning** - Ethical scanning techniques
- **Risk Assessment** - CVSS scoring methodology
- **Security Automation** - DevSecOps integration

---

## 🔮 Roadmap

### 🚀 Upcoming Features

- [ ] **🔐 Advanced Authentication** - LDAP/SSO integration
- [ ] **📱 Mobile Dashboard** - Responsive mobile interface
- [ ] **🤖 AI-Powered Analysis** - Machine learning vulnerability assessment
- [ ] **☁️ Cloud Integration** - AWS/Azure/GCP asset discovery
- [ ] **📊 Advanced Reporting** - PDF/Excel report generation
- [ ] **🔄 Patch Management** - Automated patch tracking
- [ ] **🌐 Multi-Tenant Support** - Enterprise multi-organization support
- [ ] **📡 SIEM Integration** - Splunk, ELK, QRadar connectors
- [ ] **🎭 Compliance Reporting** - PCI DSS, SOX, HIPAA templates
- [ ] **🐳 Container Security** - Docker/Kubernetes vulnerability scanning

### 🎯 Long-term Vision

Transform this system into the **ultimate enterprise vulnerability management platform** with:

- **🤖 AI-Driven Prioritization** - Intelligent risk scoring
- **🌍 Global Threat Intelligence** - Real-time threat feeds
- **🎭 Zero-Day Detection** - Advanced vulnerability research
- **📊 Predictive Analytics** - Vulnerability trend analysis
- **🛡️ Automated Remediation** - Self-healing security infrastructure

---

## ⚠️ Legal Notice

### 🚨 IMPORTANT DISCLAIMER

```
⚠️  WARNING: FOR AUTHORIZED TESTING ONLY!

This system is designed exclusively for:
✅ Authorized vulnerability assessments
✅ Enterprise security monitoring
✅ Compliance auditing
✅ Security research and education

🚫 PROHIBITED USES:
❌ Unauthorized network scanning
❌ Malicious vulnerability exploitation
❌ Illegal system access
❌ Data theft or system damage

By using this system, you agree to:
• Obtain proper authorization before scanning
• Comply with all applicable laws and regulations
• Use responsibly and ethically
• Respect network owners' policies
```

### 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

### 🎯 Inspiration & Credits

- **🛡️ Security Community** - For continuous innovation in vulnerability management
- **🔍 NIST NVD** - National Vulnerability Database integration
- **🎨 Cyberpunk Aesthetics** - Matrix and cyberpunk culture inspiration
- **🐍 Python Security Libraries** - nmap-python, requests, SQLAlchemy
- **🌐 Flask Framework** - For robust web application capabilities

### 🏆 Special Thanks

- **Enterprise Security Teams** - For real-world requirements and feedback
- **Open Source Security Tools** - Nmap, OpenVAS, and vulnerability scanners
- **CVE/CWE Communities** - For standardized vulnerability classification
- **Ethical Security Researchers** - For responsible disclosure practices

---

## 📞 Support & Contact

### 🆘 Getting Help

- **📋 Issues**: [GitHub Issues](https://github.com/Jybhavsar12/vuln-management-system/issues)
- **💬 Discussions**: [GitHub Discussions](https://github.com/Jybhavsar12/vuln-management-system/discussions)
- **📧 Email**: jyotbhavsar2003@gmail.com
- **🐦 Twitter**: [@jyotbhavsar](https://twitter.com/jyotbhavsar)

### 🎯 Professional Services

- **🏢 Enterprise Deployment** - Custom implementation and training
- **🔧 Custom Development** - Feature development and integration
- **🛡️ Security Consulting** - Vulnerability management best practices
- **📊 Compliance Auditing** - Regulatory compliance assistance

---

<div align="center">

## 🛡️ Ready to Secure Your Enterprise?

**Deploy the vulnerability management system and start securing your infrastructure in under 60 seconds!**

```bash
git clone https://github.com/Jybhavsar12/vuln-management-system.git
cd vuln-management-system && chmod +x deploy.sh && ./deploy.sh
python3 app.py
```

**🎯 Access Dashboard: http://localhost:5001**

---

**Made with ❤️ and ☕ for the Cybersecurity Community**

*Securing enterprises, one vulnerability at a time.*

</div>