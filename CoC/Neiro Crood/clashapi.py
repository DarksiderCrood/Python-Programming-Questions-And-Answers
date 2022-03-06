import requests
import clashapi

tokens = clashapi.coc("email", "password")

response = requests.get(url="https://api.clashofclans.com/v1/clans/%23208GJG2J", headers={"Accept": "application/json", "authorization": f"Bearer {tokens[0]}"})
print(response.json())