import requests
r = requests.get("https://api.github.com",auth=("lao605","lao1994110"))

print r.status_code
print r.headers["content-type"]