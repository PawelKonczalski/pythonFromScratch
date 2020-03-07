import requests

response = requests.get('https://videokurs.pl/')

print(response.status_code)
