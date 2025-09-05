#!/usr/bin/env python3
from flask import Flask, render_template, request, jsonify
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import os
from datetime import timedelta

from core.database import init_db
from api.assets import assets_bp
from api.vulnerabilities import vulns_bp
from api.scans import scans_bp
from web.dashboard import dashboard_bp

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'vuln-mgmt-secret-key')
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'jwt-secret')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=24)
    
    # Extensions
    jwt = JWTManager(app)
    CORS(app)
    
    # Initialize database
    init_db()
    
    # Register blueprints
    app.register_blueprint(assets_bp, url_prefix='/api/assets')
    app.register_blueprint(vulns_bp, url_prefix='/api/vulnerabilities')
    app.register_blueprint(scans_bp, url_prefix='/api/scans')
    app.register_blueprint(dashboard_bp, url_prefix='/')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5001)
