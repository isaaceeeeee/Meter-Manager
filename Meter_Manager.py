# Meter Manager 

import requests
import json
import pandas as pd

url = "https://www.meteronline.co.uk/api/v1/meter/meters"
headers = {
    "Accept": "application/json",
    "Authorization": "AUTHORISATION_KEY" # Replace AUTHORISATION_KEY with your own auth key
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()  
    print(json.dumps(data, indent=4))

    df = pd.DataFrame(data)
    print(df.head())
else:
    print(f"Error: {response.status_code} - {response.text}")

url = f"https://www.meteronline.co.uk/api/v1/meter/{meter}/half-hourly-readings?from=2024-04-01T00%3A00&to=2024-04-30T23%3A30"
headers = {
    "Accept": "application/json",
    "Authorization": "AUTHORISATION_KEY" # Replace AUTHORISATION_KEY with your own auth key
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()  
    print(json.dumps(data, indent=4))
    
    df = pd.DataFrame(data)
    print(df.head())
else:
    print(f"Error: {response.status_code} - {response.text}")
