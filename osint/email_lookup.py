import requests

def email_breach_lookup(email):
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {"hibp-api-key": "your-api-key", "User-Agent": "OSINT-Toolkit"}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            breaches = response.json()
            return [breach['Name'] for breach in breaches]
        elif response.status_code == 404:
            return ["No breaches found for this email."]
        else:
            return [f"Error: {response.status_code}"]
    except requests.RequestException as e:
        return [f"Error: {str(e)}"]

