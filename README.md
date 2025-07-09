# Anime-ETL-Dashboard-
ETL pipeline and Streamlit dashboard for popular anime using Jikan API

# 🌸 Popular Anime ETL Dashboard

A complete end-to-end ETL pipeline using [Jikan API](https://jikan.moe/), Apache Airflow, and Streamlit to fetch, transform, and display top anime data from MyAnimeList.

## 📌 Features

- 🔄 ETL pipeline using Python and Airflow
- 🐍 Data stored in SQLite database
- 📊 Interactive Streamlit dashboard using Plotly
- 🎬 Filters by year, score, studio, and top anime list

## 🛠️ Technologies Used

- Python
- Apache Airflow
- Pandas, Requests
- SQLite
- Streamlit
- Plotly


## 📦 How to Run This Project

This project is built using Docker + Apache Airflow and visualized using Streamlit. Follow these steps to run the complete pipeline and dashboard:

---

### 🐳 1. Start the ETL Pipeline with Docker Compose

Make sure Docker is installed and running.

```bash
docker-compose up -d
```

### 2. Open the Airflow UI

Navigate to: http://localhost:8080

- Login with default credentials 

- Find the DAG named: Popular_anime_pipeline

- Click the toggle to turn it on

- Then click Trigger DAG (play button ▶️)

Airflow will:

- Extract top anime data from the Jikan API

- Transform the data

- Load it into a local SQLite database + CSV file in the /data folder

### 📊 3. Run the Streamlit Dashboard



```bash
streamlit run airflow/Scripts/dashboard.py
```

![Screenshot 2025-07-09 190512](https://github.com/user-attachments/assets/678989ce-8907-4b8b-81d1-364fe9dee2a6)
![Screenshot 2025-07-09 190908](https://github.com/user-attachments/assets/8b8b2852-b9f7-4931-98bc-062d20595723)
