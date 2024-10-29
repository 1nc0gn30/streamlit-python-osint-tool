import requests

def ip_geolocation(ip):
    """Fetch geolocation data for an IP address (IPv4 or IPv6)."""
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'success':
            return {
                "ip": data['query'],
                "city": data.get('city', 'N/A'),
                "region": data.get('regionName', 'N/A'),
                "country": data.get('country', 'N/A'),
                "lat": data.get('lat'),
                "lon": data.get('lon'),
                "isp": data.get('isp', 'N/A'),
            }
    return None
