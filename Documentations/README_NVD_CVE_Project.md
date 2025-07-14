# 🔐 NVD CVE Assessment Project

This project retrieves CVE (Common Vulnerabilities and Exposures) data from the NVD API, stores it in a local SQLite database, exposes a set of RESTful APIs, and displays the data in a frontend UI using HTML/CSS/JavaScript.

---

## 📁 Project Structure

```
NVD_CVE_Project/
├── backend/           # FastAPI backend (API + database)
├── frontend/          # Static HTML/CSS/JS frontend
├── screenshots/       # Screenshots of working UI/API
└── README.md          # This file
```

---

## ⚙️ Backend Setup (FastAPI + SQLite)

### 1. 🔽 Navigate to Backend Folder
```bash
cd NVD_CVE_Project/backend
```

### 2. 🧱 Create Virtual Environment (optional but recommended)
```bash
python -m venv venv
# Activate venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. 📦 Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. 🔁 Fetch CVE Data from NVD API
This will:
- Create a SQLite database `cves.db`
- Fetch CVEs using the NVD API
- Store them locally

```bash
python sync_job.py
```

⚠️ **Note**: You may receive a rate limit error after 1900–2000 records. That’s okay — the app still works.

### 5. 🚀 Run FastAPI Server
```bash
python main.py
```

Access the API here:  
📘 http://127.0.0.1:8000/docs

---

## 🌐 Frontend Setup (Static HTML + JS)

### 1. 🔽 Navigate to Frontend Folder
```bash
cd NVD_CVE_Project/frontend
```

### 2. 📡 Start Local HTTP Server (Port 5500)
```bash
python -m http.server 5500
```

### 3. 🔍 Open Frontend UI in Browser
Visit:  
👉 http://localhost:5500/index.html

This loads the CVE list by calling the backend API at `http://127.0.0.1:8000/cves/list`.

---

## 📸 Screenshots (Add to `/screenshots` folder)

| Screenshot              | Description                       |
|-------------------------|-----------------------------------|
| `cve_list_ui.png`       | CVE List table with records       |
| `cve_details_ui.png`    | CVE detail page with scores       |
| `api_docs.png`          | Swagger API docs (`/docs`)        |
| `terminal_sync.png`     | Terminal showing sync_job.py run  |
| `terminal_server.png`   | Terminal showing FastAPI running  |

---

## 📡 API Endpoints

| Method | URL                                  | Description                          |
|--------|--------------------------------------|--------------------------------------|
| GET    | `/cves/list`                         | Fetch all CVEs (limit 100)           |
| GET    | `/cves/{cve_id}`                     | Get details of a specific CVE        |
| GET    | `/cves/by-year/{year}`               | Filter CVEs by year (e.g. 2023)      |
| GET    | `/cves/score-above/{score}`          | CVEs with score ≥ given value        |
| GET    | `/cves/modified-within/{days}`       | CVEs modified in the last N days     |

Test APIs here:  
👉 http://127.0.0.1:8000/docs

---

## ✅ Submission Checklist

- [x] Code pushed to GitHub
- [x] Working UI
- [x] Backend running locally
- [x] Screenshots added in `/screenshots`
- [x] This `README.md` file included

---

## 🛠️ Notes

- If you get a 404 error in the browser console for `/cves/list`, make sure `script.js` is calling the correct API:
  ```js
  fetch("http://127.0.0.1:8000/cves/list")
  ```
- Ensure FastAPI server is running **before** opening the frontend.
- You can hard refresh the browser with **Ctrl+Shift+R** if JS updates aren’t applied.

---

## 🤝 Contact

For any questions or clarification, feel free to reach out to the Securin team.
