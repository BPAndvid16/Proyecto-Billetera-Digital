import requests
import time
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

Coins = {}

def call()-> dict:

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
      'start':'1',
      'limit':'3',
      'convert':'USD'
    }
    headers = {
      'Accepts': 'application/json',    
      'X-CMC_PRO_API_KEY': '4876cb54-a094-4abb-ad1a-67ee48896912',  
    }


    json = requests.get(url, params = parameters, headers = headers).json()

    Coins["BTC"] = [json["data"][0]["name"] ,json["data"][0]["quote"]["USD"]["price"]]
    Coins["ETH"] = [json["data"][1]["name"] ,json["data"][1]["quote"]["USD"]["price"]] 
    Coins["USDT"] = [json["data"][2]["name"], json["data"][2]["quote"]["USD"]["price"]]

    return Coins