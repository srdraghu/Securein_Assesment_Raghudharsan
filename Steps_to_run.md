# NVD CVE Assessment Project

## Setup Instructions

1. Create a virtual environment

2. Run `pip install -r backend/requirements.txt`

3. Run `python backend/sync_job.py` to populate database

4. Start API with `python backend/main.py` to backend server  Test API Json File here : http://127.0.0.1:8000/docs

5. Open new terminal, navigate to Frontend folder cd/Desktop/NVD_CVE_Project/frontend

6. python -m http.server 5500     -> Start local server with this command

7. Run index.html file to UI and  ->  Try Ctrl + Shift + R  -<  if not fetching data 
