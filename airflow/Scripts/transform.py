
import pandas as pd
import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
data_path = os.path.join(project_root, 'data')

def transform_data():
    with open(os.path.join(data_path, "raw_data.json"), "r") as f:
        data = json.load(f)

    anime_data =[]
    for anime in data['data']:
        dic = {
        'title':anime['title'],
        'image':anime['images']['jpg']['image_url'],
        'score': anime['score'],
        'rank': anime['rank'],
        'year' : anime['year'],
        'synopsis': anime['synopsis'],
        'episodes': anime['episodes'],
        'studio': anime['studios'][0]['name'] 
        }
        anime_data.append(dic)

    df = pd.DataFrame(anime_data)
    df.to_csv(os.path.join(data_path, "anime_data.csv"), index=False)
    print("✅ Data transformed and saved. anime_data.csv")

if __name__ == "__main__":
    transform_data()