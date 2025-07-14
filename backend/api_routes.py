from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import CVE
from schemas import CVESchema
from typing import List
from datetime import datetime, timedelta

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/cves/list", response_model=List[CVESchema])
def list_cves(db: Session = Depends(get_db)):
    return db.query(CVE).limit(100).all()

@router.get("/cves/{cve_id}", response_model=CVESchema)
def get_cve(cve_id: str, db: Session = Depends(get_db)):
    return db.query(CVE).filter(CVE.cve_id == cve_id).first()

@router.get("/cves/by-year/{year}", response_model=List[CVESchema])
def get_by_year(year: int, db: Session = Depends(get_db)):
    return db.query(CVE).filter(CVE.cve_id.like(f"CVE-{year}-%")).all()

@router.get("/cves/score-above/{score}", response_model=List[CVESchema])
def get_by_score(score: float, db: Session = Depends(get_db)):
    return db.query(CVE).filter((CVE.score_v2 >= score) | (CVE.score_v3 >= score)).all()

@router.get("/cves/modified-within/{days}", response_model=List[CVESchema])
def get_by_modified(days: int, db: Session = Depends(get_db)):
    threshold = datetime.utcnow() - timedelta(days=days)
    return db.query(CVE).filter(CVE.last_modified >= threshold).all()
