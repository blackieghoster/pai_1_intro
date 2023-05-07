import requests
import  jmespath

# GET
# url = r"https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json"
#
# response = requests.get(url)
#
# if response.status_code == 200:
#     print(response.json())
# else:
#     print(f"Invalid http code: {response.status_code}")


# POST
# new_url = r"https://httpbin.org/post"
# data = {"name": "natalia"}
# response = requests.post(new_url, json=data)
#
# if response.status_code == 200:
#     print(response.json())
# else:
#     print(f"Invalid http code: {response.status_code}")


# Timeout
# another_url = r"https://httpbin.org/delay/2"
# data = {"name": "natalia"}
#
# for i in range(1, 10):
#     try:
#         response = requests.post(another_url, json=data, timeout=i)
#
#         if response.status_code == 200:
#             print(response.json())
#             exit()
#         else:
#             print(f"Invalid http code: {response.status_code}")
#     except requests.exceptions.ReadTimeout:
#         print(f"Error Timeout | timeout = {i}")


# JSON1
response = requests.get("https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json")

for hero in response.json()["members"]:
    print(hero["name"])
