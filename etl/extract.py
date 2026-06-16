import requests
from config import MASSIVE_API_KEY
from dotenv import load_dotenv

def extract_gas_prices():
    URL = "https://api.collectapi.com/gasPrice/allUsaPrice"
    headers = {
        "content-type" : "application/json",
        "authorization" : MASSIVE_API_KEY
    }

    response = requests.get(URL, headers=headers)
    response.raise_for_status()

    raw_data = response.json()
    return raw_data
