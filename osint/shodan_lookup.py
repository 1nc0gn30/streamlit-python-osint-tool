import shodan

def shodan_search(ip):
    api = shodan.Shodan("your-api-key")
    try:
        host = api.host(ip)
        return {
            "IP": host['ip_str'],
            "OS": host.get('os', 'N/A'),
            "Ports": host['ports'],
            "Services": [service['product'] for service in host['data']],
        }
    except shodan.APIError as e:
        return {"Error": str(e)}

