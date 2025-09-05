#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name="vuln-management-system",
    version="1.0.0",
    description="Enterprise Vulnerability Management System",
    packages=find_packages(),
    install_requires=[
        "flask",
        "sqlalchemy==2.0.21",
        "requests==2.31.0",
        "celery==5.3.1",
        "redis==4.6.0",
        "python-nmap==0.7.1",
        "beautifulsoup4==4.12.2",
        "schedule==1.2.0",
        "cryptography==41.0.4",
        "flask-jwt-extended==4.5.2",
        "psycopg2-binary==2.9.7"
    ],
    python_requires=">=3.8",
)