from flask import Blueprint, request, jsonify
from core.database import SessionLocal, Asset
from core.scanner import VulnerabilityScanner

assets_bp = Blueprint('assets', __name__)

@assets_bp.route('/', methods=['GET'])
def get_assets():
    """Get all assets"""
    session = SessionLocal()
    assets = session.query(Asset).all()
    
    result = []
    for asset in assets:
        result.append({
            'id': asset.id,
            'hostname': asset.hostname,
            'ip_address': asset.ip_address,
            'os_type': asset.os_type,
            'criticality': asset.criticality,
            'status': asset.status,
            'last_scan': asset.last_scan.isoformat() if asset.last_scan else None
        })
    
    session.close()
    return jsonify(result)

@assets_bp.route('/discover', methods=['POST'])
def discover_assets():
    """Discover assets in network"""
    data = request.json
    network_range = data.get('network_range', '192.168.1.0/24')
    
    scanner = VulnerabilityScanner()
    discovered = scanner.discover_assets(network_range)
    
    return jsonify({
        'status': 'success',
        'discovered_count': len(discovered),
        'hosts': discovered
    })

@assets_bp.route('/<int:asset_id>', methods=['DELETE'])
def delete_asset(asset_id):
    """Delete an asset"""
    session = SessionLocal()
    asset = session.query(Asset).filter_by(id=asset_id).first()
    
    if asset:
        session.delete(asset)
        session.commit()
        session.close()
        return jsonify({'status': 'success'})
    
    session.close()
    return jsonify({'error': 'Asset not found'}), 404