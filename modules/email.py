import re

def email_osint(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if re.match(pattern, email):
        domain = email.split("@")[1]
        print("[✔] Valid email format")
        print(f"[+] Email domain: {domain}")
    else:
        print("[✖] Invalid email format")
