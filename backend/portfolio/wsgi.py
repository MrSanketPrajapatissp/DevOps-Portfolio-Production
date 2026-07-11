"""
WSGI config for portfolio project.
"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

application = get_wsgi_application()

# ─── SELF-PING KEEP-ALIVE DAEMON FOR RENDER FREE TIER ──────
def self_ping():
    # Wait for the WSGI server to spin up fully
    time.sleep(15)
    external_url = os.environ.get('RENDER_EXTERNAL_URL')
    if not external_url:
        url = "http://127.0.0.1:8000/api/hero/"
    else:
        external_url = external_url.rstrip('/')
        url = f"{external_url}/api/hero/"

    print(f"[Self-Ping] Starting keep-alive daemon thread for: {url}")
    while True:
        try:
            res = requests.get(url, timeout=10)
            print(f"[Self-Ping] Status: {res.status_code} - Keep-alive ping successful.")
        except Exception as e:
            print(f"[Self-Ping] Error pinging endpoint: {e}")
        # Sleep for 10 minutes (600 seconds)
        time.sleep(600)

if os.environ.get('RENDER') == 'true' or os.environ.get('ENABLE_SELF_PING') == 'true':
    import threading
    import time
    import requests
    threading.Thread(target=self_ping, daemon=True).start()
