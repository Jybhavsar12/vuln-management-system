from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///vuln_management.db')

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Asset(Base):
    __tablename__ = "assets"
    
    id = Column(Integer, primary_key=True, index=True)
    hostname = Column(String(255), nullable=False)
    ip_address = Column(String(45), nullable=False)
    os_type = Column(String(100))
    os_version = Column(String(100))
    asset_type = Column(String(50))  # server, workstation, network_device
    criticality = Column(String(20))  # critical, high, medium, low
    owner = Column(String(100))
    location = Column(String(100))
    last_scan = Column(DateTime)
    status = Column(String(20), default='active')
    created_at = Column(DateTime, default=datetime.utcnow)

class Vulnerability(Base):
    __tablename__ = "vulnerabilities"
    
    id = Column(Integer, primary_key=True, index=True)
    cve_id = Column(String(20), unique=True, nullable=False)
    title = Column(String(500), nullable=False)
    description = Column(Text)
    severity = Column(String(20))  # critical, high, medium, low
    cvss_score = Column(Float)
    published_date = Column(DateTime)
    modified_date = Column(DateTime)
    affected_software = Column(Text)
    solution = Column(Text)
    references = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

def init_db():
    Base.metadata.create_all(bind=engine)
    print("[+] Database initialized")