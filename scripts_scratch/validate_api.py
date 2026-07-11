import os
import sys
import django
import json

# Setup Django environment
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from django.test import Client

def test_endpoint(client, path):
    print(f"\n================ GET: {path} ================")
    response = client.get(path)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        try:
            data = response.json()
            print(json.dumps(data, indent=2))
        except Exception as e:
            print(f"Failed to parse JSON response: {e}")
            print(response.content[:500])
    else:
        print(response.content[:500])

def main():
    client = Client()
    endpoints = [
        '/api/hero/',
        '/api/summary/',
        '/api/social-links/',
        '/api/resume/',
        '/api/skills/',
        '/api/projects/',
        '/api/certifications/',
        '/api/experience/',
        '/api/showcases/'
    ]
    for endpoint in endpoints:
        try:
            test_endpoint(client, endpoint)
        except Exception as e:
            print(f"Error testing {endpoint}: {e}")

if __name__ == '__main__':
    main()
