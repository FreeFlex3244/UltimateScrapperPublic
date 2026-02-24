document.addEventListener('DOMContentLoaded', () => {
    const scrapeForm = document.getElementById('scrape-form');
    const startBtn = document.getElementById('btn-start');
    const stopBtn = document.getElementById('btn-stop');
    const clearBtn = document.getElementById('btn-clear');
    const statusBadge = document.getElementById('status-badge');
    const statusText = document.getElementById('status-text');
    const filesFound = document.getElementById('files-found');
    const currentUrl = document.getElementById('current-url');
    const progressSection = document.getElementById('progress-section');

    const searchBtn = document.getElementById('btn-search');
    const searchQuery = document.getElementById('search-query');
    const searchExt = document.getElementById('search-ext');
    const resultsBody = document.getElementById('results-body');
    const copyAllBtn = document.getElementById('btn-copy-all');

    let pollInterval = null;

    // Start Scraping
    scrapeForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const url = document.getElementById('url').value;
        const depth = document.getElementById('depth').value;
        const extensions = document.getElementById('extensions').value;

        if (!url || !depth || !extensions) {
            alert("Please fill all fields!");
            return;
        }

        try {
            const res = await fetch('/api/start', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ url, depth, extensions })
            });
            const data = await res.json();

            if (data.status === 'success') {
                startBtn.disabled = true;
                stopBtn.disabled = false;
                progressSection.style.display = 'block';
                startPolling();
            } else {
                alert(data.message);
            }
        } catch (err) {
            console.error(err);
        }
    });

    // Stop Scraping
    stopBtn.addEventListener('click', async () => {
        try {
            await fetch('/api/stop', { method: 'POST' });
            stopBtn.disabled = true;
            statusText.textContent = "Stopping...";
        } catch (err) {
            console.error(err);
        }
    });

    // Clear DB
    clearBtn.addEventListener('click', async () => {
        if (!confirm("Are you sure you want to delete all indexed files?")) return;
        try {
            const res = await fetch('/api/clear', { method: 'POST' });
            const data = await res.json();
            if (data.status === 'success') {
                alert("Database cleared!");
                resultsBody.innerHTML = '';
            } else {
                alert(data.message);
            }
        } catch (err) {
            console.error(err);
        }
    });

    // Poll Status
    function startPolling() {
        if (pollInterval) clearInterval(pollInterval);

        pollInterval = setInterval(async () => {
            try {
                const res = await fetch('/api/status');
                const data = await res.json();

                statusBadge.textContent = data.status;
                filesFound.textContent = data.found;
                currentUrl.textContent = data.current_url || "";

                if (data.status === 'Running') {
                    statusBadge.className = 'badge bg-warning text-dark';
                    startBtn.disabled = true;
                    stopBtn.disabled = false;
                } else if (data.status === 'Completed' || data.status === 'Stopped') {
                    statusBadge.className = 'badge bg-success';
                    startBtn.disabled = false;
                    stopBtn.disabled = true;
                    clearInterval(pollInterval);
                } else if (data.status.startsWith('Error')) {
                    statusBadge.className = 'badge bg-danger';
                    startBtn.disabled = false;
                    stopBtn.disabled = true;
                    clearInterval(pollInterval);
                }

            } catch (err) {
                console.error(err);
            }
        }, 1000);
    }

    // Search
    async function performSearch() {
        const query = searchQuery.value;
        const ext = searchExt.value;

        // Loading state
        searchBtn.disabled = true;
        const originalContent = searchBtn.innerHTML;
        searchBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Searching...';

        try {
            const res = await fetch(`/api/search?q=${encodeURIComponent(query)}&ext=${encodeURIComponent(ext)}`);
            const data = await res.json();
            renderResults(data.results);
        } catch (err) {
            console.error(err);
        } finally {
            searchBtn.disabled = false;
            searchBtn.innerHTML = originalContent;
        }
    }

    searchBtn.addEventListener('click', performSearch);
    searchQuery.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') performSearch();
    });

    function isValidUrl(string) {
        try {
            const url = new URL(string);
            return url.protocol === "http:" || url.protocol === "https:";
        } catch (_) {
            return false;
        }
    }

    function renderResults(files) {
        resultsBody.innerHTML = '';
        if (files.length === 0) {
            document.getElementById('no-results').style.display = 'block';
            return;
        }
        document.getElementById('no-results').style.display = 'none';

        files.forEach(file => {
            const tr = document.createElement('tr');

            // --- Filename Cell ---
            const tdFilename = document.createElement('td');
            const aFilename = document.createElement('a');
            aFilename.target = "_blank";
            aFilename.className = "text-light text-decoration-none";
            aFilename.textContent = file.filename; // SAFE: textContent used instead of innerHTML

            if (isValidUrl(file.url)) {
                aFilename.href = file.url;
            } else {
                aFilename.href = '#';
                aFilename.title = 'Invalid URL';
                aFilename.onclick = (e) => e.preventDefault();
            }

            tdFilename.appendChild(aFilename);
            tr.appendChild(tdFilename);

            // --- Extension Cell ---
            const tdExt = document.createElement('td');
            const spanExt = document.createElement('span');
            spanExt.className = "badge bg-secondary";
            spanExt.textContent = file.extension; // SAFE: textContent
            tdExt.appendChild(spanExt);
            tr.appendChild(tdExt);

            // --- Depth Cell ---
            const tdDepth = document.createElement('td');
            tdDepth.textContent = file.depth; // SAFE: textContent
            tr.appendChild(tdDepth);

            // --- Action Cell ---
            const tdAction = document.createElement('td');
            tdAction.className = "text-end";

            // Copy Button
            const btnCopy = document.createElement('button');
            btnCopy.className = "btn btn-sm btn-outline-warning copy-btn";
            btnCopy.setAttribute('data-url', file.url);
            btnCopy.setAttribute('aria-label', `Copy link for ${file.filename}`);
            btnCopy.title = "Copy link";

            const iconCopy = document.createElement('i');
            iconCopy.className = "fas fa-copy";
            btnCopy.appendChild(iconCopy);

            // Add event listener directly
            btnCopy.addEventListener('click', () => {
                const url = file.url;
                navigator.clipboard.writeText(url).then(() => {
                    iconCopy.className = 'fas fa-check';
                    setTimeout(() => {
                        iconCopy.className = 'fas fa-copy';
                    }, 1000);
                });
            });

            tdAction.appendChild(btnCopy);

            // Download Button
            const btnDownload = document.createElement('a');
            btnDownload.className = "btn btn-sm btn-primary ms-1";
            btnDownload.setAttribute('download', '');
            btnDownload.setAttribute('aria-label', `Download ${file.filename}`);
            btnDownload.title = "Download file";

            if (isValidUrl(file.url)) {
                btnDownload.href = file.url;
            } else {
                btnDownload.href = '#';
                btnDownload.onclick = (e) => e.preventDefault();
            }

            const iconDownload = document.createElement('i');
            iconDownload.className = "fas fa-download";
            btnDownload.appendChild(iconDownload);
            tdAction.appendChild(btnDownload);

            tr.appendChild(tdAction);
            resultsBody.appendChild(tr);
        });
    }

    // Copy All
    copyAllBtn.addEventListener('click', () => {
        const links = Array.from(document.querySelectorAll('#results-body a.text-light'))
            .map(a => a.href)
            .join('\n');

        if (!links) return;

        navigator.clipboard.writeText(links).then(() => {
            copyAllBtn.textContent = 'Copied!';
            setTimeout(() => {
                copyAllBtn.innerHTML = '<i class="fas fa-copy me-2"></i>Copy All Links';
            }, 2000);
        });
    });
});
