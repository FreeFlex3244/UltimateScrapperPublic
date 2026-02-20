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

        try {
            const res = await fetch(`/api/search?q=${encodeURIComponent(query)}&ext=${encodeURIComponent(ext)}`);
            const data = await res.json();
            renderResults(data.results);
        } catch (err) {
            console.error(err);
        }
    }

    searchBtn.addEventListener('click', performSearch);
    searchQuery.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') performSearch();
    });

    function renderResults(files) {
        resultsBody.innerHTML = '';
        if (files.length === 0) {
            document.getElementById('no-results').style.display = 'block';
            return;
        }
        document.getElementById('no-results').style.display = 'none';

        files.forEach(file => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td><a href="${file.url}" target="_blank" class="text-light text-decoration-none">${file.filename}</a></td>
                <td><span class="badge bg-secondary">${file.extension}</span></td>
                <td>${file.depth}</td>
                <td class="text-end">
                    <button class="btn btn-sm btn-outline-warning copy-btn" data-url="${file.url}">
                        <i class="fas fa-copy"></i>
                    </button>
                    <a href="${file.url}" class="btn btn-sm btn-primary" download>
                        <i class="fas fa-download"></i>
                    </a>
                </td>
            `;
            resultsBody.appendChild(tr);
        });

        // Add copy listeners
        document.querySelectorAll('.copy-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const url = e.currentTarget.getAttribute('data-url');
                navigator.clipboard.writeText(url).then(() => {
                    const icon = e.currentTarget.querySelector('i');
                    icon.className = 'fas fa-check';
                    setTimeout(() => {
                        icon.className = 'fas fa-copy';
                    }, 1000);
                });
            });
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
