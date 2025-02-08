import requests

url = "https://eth-mainnet.g.alchemy.com/v2/ZjwIZLdgUrtPJxn5bty0oZQKg_qjpd7q/getNFTs/"
params = {"owner": "vitalik.eth"}

response = requests.get(url, params=params)
data = response.json()

print(data)
