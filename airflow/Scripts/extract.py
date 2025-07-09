

import requests
import json
import os

url = "https://api.jikan.moe/v4/top/anime?filter=bypopularity"

script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
raw_data_path = os.path.join(project_root, 'data')

def fetch_anime_data():
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        with open(os.path.join(raw_data_path, "raw_data.json"), "w") as f:
            json.dump(data, f, indent=2)
        print("✅ Data extracted and saved.")
    else:
        print("❌ Failed to fetch data:", response.status_code)

if __name__ == "__main__":
    fetch_anime_data()