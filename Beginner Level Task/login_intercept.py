import requests

URL = "http://testphp.vulnweb.com/login.php"

USERNAME = "test"
PASSWORD = "test123"

data = {
    "uname": USERNAME,  
    "pass": PASSWORD,
    "submit": "Login"
}

response = requests.post(URL, data=data)

if "incorrect" in response.text.lower():
    print("[!] Login failed. Try different credentials.")
else:
    print("[+] Login successful! Credentials sent:")
    print(f"    Username: {USERNAME}")
    print(f"    Password: {PASSWORD}")
