from flask import Blueprint, request, jsonify
from core.database import SessionLocal, Asset
from core.scanner import VulnerabilityScanner
from datetime import datetime

scans_bp = Blueprint('scans', __name__)

@scans_bp.route('/start', methods=['POST'])
def start_scan():
    """Start vulnerability scan"""
    data = request.json
    target = data.get('target', '192.168.1.0/24')
    scan_type = data.get('type', 'discovery')
    
    scanner = VulnerabilityScanner()
    
    if scan_type == 'discovery':
        results = scanner.discover_assets(target)
        return jsonify({
            'status': 'success',
            'scan_type': 'discovery',
            'results': results,
            'timestamp': datetime.now().isoformat()
        })
    
    elif scan_type == 'port':
        results = scanner.port_scan(target)
        return jsonify({
            'status': 'success',
            'scan_type': 'port',
            'results': str(results),
            'timestamp': datetime.now().isoformat()
        })
    
    return jsonify({'error': 'Invalid scan type'}), 400

@scans_bp.route('/status', methods=['GET'])
def scan_status():
    """Get scan status"""
    return jsonify({
        'status': 'idle',
        'last_scan': datetime.now().isoformat(),
        'active_scans': 0
    })

@scans_bp.route('/history', methods=['GET'])
def scan_history():
    """Get scan history"""
    return jsonify({
        'scans': [
            {
                'id': 1,
                'type': 'discovery',
                'target': '192.168.1.0/24',
                'timestamp': datetime.now().isoformat(),
                'status': 'completed',
                'results_count': 5
            }
        ]
    })