import requests

url = "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json"

response = requests.get(url)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Invalid http code: {response.status_code}")
