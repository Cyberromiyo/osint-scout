import requests

def username_osint(username):
    sites = {
        "Instagram": f"https://www.instagram.com/{username}",
        "GitHub": f"https://github.com/{username}",
        "Twitter": f"https://twitter.com/{username}"
    }

    print(f"[+] Searching username: {username}")

    for site, url in sites.items():
        r = requests.get(url)
        if r.status_code == 200:
            print(f"[✔] Found on {site}: {url}")
        else:
            print(f"[✖] Not Found on {site}")
