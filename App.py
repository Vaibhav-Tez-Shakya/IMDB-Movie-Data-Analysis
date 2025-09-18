import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(page_title="IMDB Movie Analysis", layout="wide")

# Load dataset
@st.cache_data
def load_data():
    data = pd.read_csv("IMDB Dataset.csv")

    data['Released_Year'] = pd.to_numeric(data['Released_Year'], errors='coerce')

    data = data.dropna(subset=['Released_Year'])

    data['Released_Year'] = data['Released_Year'].astype(int)

    data['Decade'] = (data['Released_Year'] // 10) * 10
    return data

data = load_data()

st.title("🎬 IMDB Top 1000 Movie Analysis")

if st.checkbox("Show Raw Data"):
    st.write(data.head())

st.sidebar.header("Filters")
selected_genre = st.sidebar.multiselect("Select Genre", options=data['Genre'].unique())
selected_director = st.sidebar.multiselect("Select Director", options=data['Director'].unique())

filtered_data = data.copy()
if selected_genre:
    filtered_data = filtered_data[filtered_data['Genre'].isin(selected_genre)]
if selected_director:
    filtered_data = filtered_data[filtered_data['Director'].isin(selected_director)]

st.subheader("Dataset Info")
st.write(f"Total Movies: {len(filtered_data)}")

# Top 10 movies by IMDB Rating
st.subheader("Top 10 Movies by IMDB Rating")
top10 = filtered_data.sort_values(by="IMDB_Rating", ascending=False).head(10)
st.table(top10[['Series_Title', 'Released_Year', 'IMDB_Rating', 'Genre', 'Director']])

st.subheader("IMDB Ratings Distribution")
fig, ax = plt.subplots()
sns.histplot(filtered_data['IMDB_Rating'], bins=20, kde=True, ax=ax, color="skyblue")
st.pyplot(fig)

st.subheader("Movies per Decade")
fig, ax = plt.subplots(figsize=(10, 5))
sns.countplot(x='Decade', data=filtered_data, ax=ax, palette="Set2")
plt.xticks(rotation=45)
st.pyplot(fig)

st.subheader("Average IMDB Rating by Genre")
avg_genre = filtered_data.groupby('Genre')['IMDB_Rating'].mean().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x=avg_genre.index, y=avg_genre.values, ax=ax, palette="viridis")
plt.xticks(rotation=90)
st.pyplot(fig)

st.subheader("Top 10 Directors by Movie Count")
top_directors = filtered_data['Director'].value_counts().head(10)
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=top_directors.values, y=top_directors.index, ax=ax, palette="coolwarm")
st.pyplot(fig)
