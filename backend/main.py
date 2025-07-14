from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api_routes import router
import uvicorn

app = FastAPI(title="NVD CVE API Project")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to ["http://localhost:5500"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
