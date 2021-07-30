import requests

url = 'https://api.daktarz.com/User/forgotPassword'

data = {'phoneNo': "7986485146", 'countryCode': "+91"}

response = requests.post(url,data = data).text

print(response)