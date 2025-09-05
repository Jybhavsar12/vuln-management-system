#!/bin/bash

echo "🛡️ Vulnerability Management System - Deployment"
echo "================================================"

# Check Python 3
if ! command -v python3 &> /dev/null; then
    echo "[-] Python 3 is required"
    exit 1
fi

echo "[+] Python 3 found: $(python3 --version)"

# Create directory structure
echo "[+] Creating directory structure..."
mkdir -p {api,core,web,templates,static,logs,reports,config}

# Install dependencies
echo "[+] Installing dependencies..."
pip3 install -r requirements.txt

# Initialize database
echo "[+] Initializing database..."
python3 -c "from core.database import init_db; init_db()"

# Make executable
chmod +x app.py

echo ""
echo "🎯 Deployment Complete!"
echo ""
echo "Usage:"
echo "  Start Server: python3 app.py"
echo "  Web Dashboard: http://localhost:5001"
echo "  API Endpoints: http://localhost:5001/api/"
echo ""
echo "⚠️  For authorized security testing only!"
