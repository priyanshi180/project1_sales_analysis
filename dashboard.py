import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("data.csv")

# Dashboard title
st.title("📊 Sales Data Dashboard")

# Show raw data
st.subheader("Raw Data")
st.write(df)

# Sales by region
st.subheader("Sales by Region")
region_sales = df.groupby("region")["sales"].sum().reset_index()
st.bar_chart(region_sales.set_index("region"))

# Profit distribution
st.subheader("Profit Distribution")
st.line_chart(df["profit"])
