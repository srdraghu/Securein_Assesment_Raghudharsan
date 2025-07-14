from cve_fetcher import fetch_and_store_cves
from models import CVE
from database import engine
from database import Base

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    fetch_and_store_cves()
