import requests

url = 'https://api.daktarz.com/User/forgotPassword'

phone = str(int(input()))

data = {'phoneNo': phone, 'countryCode': "+91"}

response = requests.post(url,data = data).text

print(response)
