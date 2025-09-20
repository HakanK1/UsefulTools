import requests
import json

api_key = "42c46fa1446bde15049307f8"
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/" # Currency takes place at the end

exchanged_currency = input("Currency to be exchanged: ")
purchased_currency = input("Currency to be purchased: ")
amount = int(input(f"How much {exchanged_currency}: "))

infos = requests.get(api_url +exchanged_currency)
infos_json = json.loads(infos.text)
print(f"1 {exchanged_currency} = {infos_json["conversion_rates"][purchased_currency]} {purchased_currency}")
result = amount * infos_json["conversion_rates"][purchased_currency]
print(f"{amount} {exchanged_currency} = {result} {purchased_currency}")