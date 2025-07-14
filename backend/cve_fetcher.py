import requests
from database import SessionLocal, engine
from models import CVE
from sqlalchemy.orm import Session
from datetime import datetime
import time

def fetch_and_store_cves():
    session = SessionLocal()
    base_url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    start_index = 0
    total_results = 1

    print("🔄 Starting CVE sync from NVD API...")

    while start_index < total_results:
        print(f"📦 Fetching records from index: {start_index}")

        try:
            response = requests.get(base_url, params={
                "startIndex": start_index,
                "resultsPerPage": 100
            }, timeout=15)
            response.raise_for_status()  # Raise error for 4xx or 5xx

            try:
                data = response.json()
            except Exception as e:
                print("❌ JSON parsing failed:", e)
                print("Raw response:", response.text[:200])  # Limit preview
                break

        except requests.exceptions.RequestException as e:
            print("❌ Request failed:", e)
            break

        total_results = data.get("totalResults", 0)
        cve_items = data.get("vulnerabilities", [])

        for item in cve_items:
            try:
                cve = item.get("cve")
                cve_id = cve.get("id")
                published = cve.get("published")
                modified = cve.get("lastModified")
                desc = cve.get("descriptions", [{}])[0].get("value", "")
                score_v2 = None
                score_v3 = None

                metrics = cve.get("metrics", {})
                if "cvssMetricV2" in metrics:
                    score_v2 = metrics["cvssMetricV2"][0]["cvssData"]["baseScore"]
                if "cvssMetricV3" in metrics:
                    score_v3 = metrics["cvssMetricV3"][0]["cvssData"]["baseScore"]

                # Avoid duplicates
                exists = session.query(CVE).filter(CVE.cve_id == cve_id).first()
                if not exists:
                    new_cve = CVE(
                        cve_id=cve_id,
                        published=datetime.fromisoformat(published),
                        last_modified=datetime.fromisoformat(modified),
                        description=desc,
                        score_v2=score_v2,
                        score_v3=score_v3
                    )
                    session.add(new_cve)
            except Exception as e:
                print(f"⚠️ Skipped one CVE due to error: {e}")
                continue

        session.commit()
        print(f"✅ Fetched and stored {len(cve_items)} records.")
        start_index += 100
