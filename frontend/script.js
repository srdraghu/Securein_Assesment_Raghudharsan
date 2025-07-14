fetch("http://127.0.0.1:8000/cves/list")
    .then(res => res.json())
    .then(data => {
        const tbody = document.querySelector("#cveTable tbody");
        document.getElementById("totalCount").textContent = "Total Records: " + data.length;
        data.forEach(item => {
            const row = tbody.insertRow();
            row.innerHTML = `
                <td><a href="details.html?cve_id=${item.cve_id}">${item.cve_id}</a></td>
                <td>${new Date(item.published).toLocaleDateString()}</td>
                <td>${item.score_v2 || item.score_v3 || "N/A"}</td>
            `;
        });
    })
    .catch(error => {
        console.error("Failed to fetch CVE list:", error);
        alert("Failed to load CVE data. Is the backend running?");
    });
