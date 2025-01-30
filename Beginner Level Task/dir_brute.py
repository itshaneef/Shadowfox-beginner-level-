import requests
import threading

TARGET_URL = "http://testphp.vulnweb.com/"

DIRECTORIES = ["admin", "login", "uploads", "images", "css", "js", "includes", "backup", "phpmyadmin"]

def check_directory(directory):
    url = TARGET_URL + directory
    response = requests.get(url)

    if response.status_code == 200:
        print(f"[+] Found: {url}")
    elif response.status_code == 403:
        print(f"[!] Forbidden (403): {url}")

threads = []
for directory in DIRECTORIES:
    thread = threading.Thread(target=check_directory, args=(directory,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Scanning completed.")
