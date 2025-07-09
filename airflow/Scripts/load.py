
# load.py

import os
import pandas as pd
import sqlite3

script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
data_path = os.path.join(project_root, 'data')

def load_to_sqlite():
    df = pd.read_csv(os.path.join(data_path, "anime_data.csv"))
    conn = sqlite3.connect(os.path.join(data_path, "popular_animes.db"))
    df.to_sql("popular_animes", conn, if_exists="replace", index=False)

    conn.close()
    print("✅ Data loaded into SQLite database (popular_animes.db)")

if __name__ == "__main__":
    load_to_sqlite()