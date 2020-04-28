import requests

response=requests.get('hp.com')
print(response.status_code)
