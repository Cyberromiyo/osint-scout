import socket

def domain_osint(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"[✔] IP Address: {ip}")
    except:
        print("[✖] Unable to resolve domain")
