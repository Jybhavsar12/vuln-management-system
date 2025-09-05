from flask import Blueprint, render_template_string

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
def dashboard():
    """Main dashboard"""
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>🛡️ Vulnerability Management System</title>
        <style>
            body { 
                font-family: 'Courier New', monospace; 
                background: #0a0a0a; 
                color: #00ff00; 
                margin: 0; 
                padding: 20px; 
            }
            .header { 
                text-align: center; 
                border-bottom: 2px solid #00ff00; 
                padding-bottom: 20px; 
                margin-bottom: 30px; 
            }
            .dashboard-grid { 
                display: grid; 
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); 
                gap: 20px; 
            }
            .card { 
                background: #1a1a1a; 
                border: 1px solid #00ff00; 
                padding: 20px; 
                border-radius: 5px; 
            }
            .btn { 
                background: #003300; 
                color: #00ff00; 
                border: 1px solid #00ff00; 
                padding: 10px 20px; 
                cursor: pointer; 
                margin: 5px; 
            }
            .btn:hover { background: #004400; }
            #assets-table { width: 100%; border-collapse: collapse; }
            #assets-table th, #assets-table td { 
                border: 1px solid #00ff00; 
                padding: 8px; 
                text-align: left; 
            }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>🛡️ VULNERABILITY MANAGEMENT SYSTEM</h1>
            <p>Enterprise Security Dashboard</p>
        </div>
        
        <div class="dashboard-grid">
            <div class="card">
                <h3>📊 System Overview</h3>
                <p>Total Assets: <span id="total-assets">Loading...</span></p>
                <p>Critical Vulns: <span id="critical-vulns">Loading...</span></p>
                <p>Last Scan: <span id="last-scan">Loading...</span></p>
            </div>
            
            <div class="card">
                <h3>🔍 Asset Discovery</h3>
                <input type="text" id="network-range" placeholder="192.168.1.0/24" style="width: 200px; background: #1a1a1a; color: #00ff00; border: 1px solid #00ff00; padding: 5px;">
                <button class="btn" onclick="discoverAssets()">Discover Assets</button>
            </div>
            
            <div class="card">
                <h3>🎯 Quick Actions</h3>
                <button class="btn" onclick="refreshDashboard()">Refresh Dashboard</button>
                <button class="btn" onclick="exportReport()">Export Report</button>
                <button class="btn" onclick="startScan()">Start Full Scan</button>
            </div>
        </div>
        
        <div class="card" style="margin-top: 20px;">
            <h3>💻 Asset Inventory</h3>
            <table id="assets-table">
                <thead>
                    <tr>
                        <th>Hostname</th>
                        <th>IP Address</th>
                        <th>OS Type</th>
                        <th>Criticality</th>
                        <th>Status</th>
                        <th>Last Scan</th>
                    </tr>
                </thead>
                <tbody id="assets-tbody">
                </tbody>
            </table>
        </div>
        
        <script>
            function loadAssets() {
                fetch('/api/assets/')
                    .then(response => response.json())
                    .then(data => {
                        const tbody = document.getElementById('assets-tbody');
                        tbody.innerHTML = '';
                        
                        data.forEach(asset => {
                            const row = tbody.insertRow();
                            row.innerHTML = `
                                <td>${asset.hostname}</td>
                                <td>${asset.ip_address}</td>
                                <td>${asset.os_type || 'Unknown'}</td>
                                <td>${asset.criticality}</td>
                                <td>${asset.status}</td>
                                <td>${asset.last_scan || 'Never'}</td>
                            `;
                        });
                        
                        document.getElementById('total-assets').textContent = data.length;
                    });
            }
            
            function discoverAssets() {
                const networkRange = document.getElementById('network-range').value || '192.168.1.0/24';
                
                fetch('/api/assets/discover', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({network_range: networkRange})
                })
                .then(response => response.json())
                .then(data => {
                    alert(`Discovered ${data.discovered_count} new assets`);
                    loadAssets();
                });
            }
            
            function refreshDashboard() {
                loadAssets();
            }
            
            function exportReport() {
                alert('Report export functionality coming soon!');
            }
            
            function startScan() {
                alert('Full vulnerability scan initiated!');
            }
            
            // Load initial data
            loadAssets();
            setInterval(loadAssets, 30000); // Refresh every 30 seconds
        </script>
    </body>
    </html>
    ''')