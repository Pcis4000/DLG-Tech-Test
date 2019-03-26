import requests

r = requests.post("https://89tuws2rg3.execute-api.eu-west-2.amazonaws.com/APIGatewayLive/total",auth=("g8nxbe7ct6","SgKSotj4Ad3hPGfvPlZvI1KANRKKgGLn9p23swhw"), data={'body':[4,6,3,25,6]})
r = r.json()

print(r)
