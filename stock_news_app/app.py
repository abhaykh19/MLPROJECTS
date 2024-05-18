import requests
import streamlit as st
import pandas as pd

# API details
url = "https://share-market-news-api-india.p.rapidapi.com/marketNews"
headers = {
    "X-RapidAPI-Key": "645d82f893msh902258453429d79p1891bejsn62fa5e0cbc35",
    "X-RapidAPI-Host": "share-market-news-api-india.p.rapidapi.com"
}

# Fetch data from API
response = requests.get(url, headers=headers)

if response.status_code == 200:
    news_data = response.json()
else:
    st.error("Failed to fetch data from API")
    news_data = []

# Create DataFrame from the news data
if news_data:
    df = pd.DataFrame(news_data)
else:
    df = pd.DataFrame(columns=["title", "link", "published"])

# Streamlit app
st.title("Share Market News")
st.write("Latest news from the share market:")

# Display the table
if not df.empty:
    st.dataframe(df)
else:
    st.write("No news available at the moment.")

