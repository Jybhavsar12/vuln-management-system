from flask import Blueprint, request, jsonify
from core.database import SessionLocal, Vulnerability
from core.scanner import VulnerabilityScanner

vulns_bp = Blueprint('vulnerabilities', __name__)

@vulns_bp.route('/', methods=['GET'])
def get_vulnerabilities():
    """Get all vulnerabilities"""
    session = SessionLocal()
    vulns = session.query(Vulnerability).all()
    
    result = []
    for vuln in vulns:
        result.append({
            'id': vuln.id,
            'cve_id': vuln.cve_id,
            'title': vuln.title,
            'severity': vuln.severity,
            'cvss_score': vuln.cvss_score,
            'published_date': vuln.published_date.isoformat() if vuln.published_date else None,
            'description': vuln.description
        })
    
    session.close()
    return jsonify(result)

@vulns_bp.route('/search', methods=['POST'])
def search_vulnerabilities():
    """Search vulnerabilities by CVE ID"""
    data = request.json
    cve_id = data.get('cve_id')
    
    if not cve_id:
        return jsonify({'error': 'CVE ID required'}), 400
    
    scanner = VulnerabilityScanner()
    cve_data = scanner.fetch_cve_data(cve_id)
    
    if cve_data:
        return jsonify({'status': 'success', 'data': cve_data})
    else:
        return jsonify({'error': 'CVE not found'}), 404

@vulns_bp.route('/<int:vuln_id>', methods=['DELETE'])
def delete_vulnerability(vuln_id):
    """Delete a vulnerability"""
    session = SessionLocal()
    vuln = session.query(Vulnerability).filter_by(id=vuln_id).first()
    
    if vuln:
        session.delete(vuln)
        session.commit()
        session.close()
        return jsonify({'status': 'success'})
    
    session.close()
    return jsonify({'error': 'Vulnerability not found'}), 404