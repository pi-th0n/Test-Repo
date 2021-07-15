import requests

r = requests.get("https://pi-th0n.github.io/")
print(r.status_code)
