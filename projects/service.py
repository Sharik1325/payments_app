import requests
import json

url = 'https://sandbox.api.payulatam.com/payments-api/4.0/service.cgi'
data = {
    "language": "es",
    "command": "SUBMIT_TRANSACTION",
    "merchant": {
        "apiKey": "4Vj8eK4rloUd272L48hsrarnUA",
        "apiLogin": "pRRXKOl8ikMmt9u"
    }}


def answer():
    response = requests.post(url, headers={"Content-Type": "application/json"}, json=data)
    return response





