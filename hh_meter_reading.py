# meter_reading.py 

import requests
import json
import pandas as pd

# Amend the params to suit  
meter = "meter" # meter number
from_date = "from_date" # yyyy-mm-dd
to_date = "to_date" # yyyy-mm-dd

url = f"https://www.meteronline.co.uk/api/v1/meter/{meter}/half-hourly-readings?from={from_date}T00%3A00&to={to_date}T23%3A30"

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
