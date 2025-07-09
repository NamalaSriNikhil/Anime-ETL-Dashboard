
import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Load data
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
data_path = os.path.join(project_root, 'data','anime_data.csv')
df = pd.read_csv(data_path)

st.set_page_config(page_title="Anime Dashboard", layout="wide")
st.title("🌸 Anime Dashboard")
st.markdown("View trending, top-rated, and popular anime from MyAnimeList")

# --- Sidebar Filters ---
st.sidebar.header("📊 Filters")

years = df["year"].dropna().astype(int)
selected_year = st.sidebar.slider("Select Year", int(years.min()), int(years.max()), (2010, 2023))
selected_score = st.sidebar.slider("Minimum Score", float(df["score"].min()), float(df["score"].max()), 7.0)
studios = ["All"] + sorted(df["studio"].dropna().unique().tolist())
selected_studio = st.sidebar.selectbox("Studio", studios)

# --- Apply filters ---
filtered_df = df[
    (df["year"].between(*selected_year)) &
    (df["score"] >= selected_score)
]

if selected_studio != "All":
    filtered_df = filtered_df[filtered_df["studio"] == selected_studio]

st.subheader(f"🎬 Found {len(filtered_df)} anime")

# --- Top Rated Chart ---
top_df = filtered_df.sort_values(by="score", ascending=False).head(10)
fig = px.bar(top_df, x="title", y="score", title="Top 10 Rated Anime", color="score", text="score")
fig.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig, use_container_width=True)

# --- Display Anime Cards ---
st.subheader("📺 Anime Cards")

for index, row in filtered_df.head(12).iterrows():
    with st.container():
        cols = st.columns([1, 3])
        with cols[0]:
            st.image(row['image'], width=130)
        with cols[1]:
            st.markdown(f"### {row['title']} ({int(row['year'])})")
            st.markdown(f"**Studio:** {row['studio']} | **Episodes:** {row['episodes']} | **Score:** ⭐ {row['score']}")
            st.markdown(f"**Synopsis:** {row['synopsis'][:300]}...")
            # Optional: Add trailer if you collected trailer URLs
            # st.video(row['trailer_url'])  
