import requests

def search_username(username):
    platforms = {
        "Twitter": f"https://twitter.com/{username}",
        "GitHub": f"https://github.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}/",
    }
    results = {}

    for platform, url in platforms.items():
        try:
            response = requests.get(url)
            if response.status_code == 200:
                results[platform] = "Found"
            else:
                results[platform] = "Not Found"
        except requests.RequestException as e:
            results[platform] = f"Error: {str(e)}"

    return results

