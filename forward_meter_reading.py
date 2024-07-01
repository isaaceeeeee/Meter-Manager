# meter_reading.py 

import requests
import json
import pandas as pd

meter = "meter" # meter number
date_str = "date" # yyyy-mm-dd
url = f"https://www.meteronline.co.uk/api/v1/meter/{meter}/forward-reading?date={date_str}"

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