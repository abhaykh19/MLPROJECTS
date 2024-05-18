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
    df = pd.DataFrame(columns=["Title", "URL", "Source"])

# Streamlit app
st.title("Share Market News")
st.write("Latest news from the share market:")

# Search bar
search_query = st.text_input("Search for news:", "")

# Filter news based on search query
filtered_df = df[df["Title"].str.contains(search_query, case=False) | df["Source"].str.contains(search_query, case=False)]

# Display cards for each news item
if not filtered_df.empty:
    for i, (index, row) in enumerate(filtered_df.iterrows(), start=1):
        st.write(f"**{i}. {row['Title']}**")
        st.write(f"Source: {row['Source']}")
        st.write(f"URL: [{row['URL']}]({row['URL']})")
        st.write("---")
else:
    st.write("No news available matching the search criteria.")
