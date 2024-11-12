import requests

def test_server(url, expected_status):
    try:
        response = requests.get(url)
        if response.status_code == expected_status:
            print(f"SUCCESS: {url} returned {expected_status}")
            return True
        else:
            print(f"FAIL: {url} returned {response.status_code} instead of {expected_status}")
            return False
    except Exception as e:
        print(f"ERROR: Could not connect to {url}")
        return False

if __name__ == "__main__":
    tests = [
        ("http://nginx-server:8080", 200),
        ("http://nginx-server:8081", 404),
    ]
    results = [test_server(url, status) for url, status in tests]
    if all(results):
        exit(0)
    else:
        exit(1)
