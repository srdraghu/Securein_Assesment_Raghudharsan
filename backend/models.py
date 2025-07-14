from sqlalchemy import Column, String, Integer, DateTime, Float
from database import Base

class CVE(Base):
    __tablename__ = "cves"
    id = Column(Integer, primary_key=True, index=True)
    cve_id = Column(String, unique=True, index=True)
    published = Column(DateTime)
    last_modified = Column(DateTime)
    description = Column(String)
    score_v2 = Column(Float, nullable=True)
    score_v3 = Column(Float, nullable=True)
