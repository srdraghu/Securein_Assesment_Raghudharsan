from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CVESchema(BaseModel):
    cve_id: str
    published: datetime
    last_modified: datetime
    description: str
    score_v2: Optional[float]
    score_v3: Optional[float]

    class Config:
        orm_mode = True
