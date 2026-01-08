from banner import banner
from modules.username import username_osint
from modules.email import email_osint
from modules.domain import domain_osint

banner()

print("1. Username OSINT")
print("2. Email OSINT")
print("3. Domain OSINT")

choice = input("Select option: ")

if choice == "1":
    u = input("Enter username: ")
    username_osint(u)

elif choice == "2":
    e = input("Enter email: ")
    email_osint(e)

elif choice == "3":
    d = input("Enter domain: ")
    domain_osint(d)

else:
    print("Invalid choice")
