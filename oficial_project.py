import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")

df_reviews = pd.read_csv("web_project\customer reviews.csv")
df_100_top_books = pd.read_csv("web_project\Top-100 Trending Books.csv")

price_max = df_100_top_books["book price"].max()
price_min = df_100_top_books["book price"].min()

max_price = st.sidebar.slider("Price Range", price_min, price_max, price_max)
df_books = df_100_top_books[df_100_top_books["book price"] <= max_price]

px.bar(df_books["year of publication"].value_counts())

df_books