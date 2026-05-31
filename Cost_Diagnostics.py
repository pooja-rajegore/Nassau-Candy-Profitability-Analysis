import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

# Load Data

df = pd.read_csv('final_nassau_data.csv')

st.title("⚠ Cost vs Margin Diagnostics")

# Scatter Plot

scatter_fig = px.scatter(
    df,
    x='sales',
    y='cost',
    size='gross_profit',
    color='business_recommendation',
    hover_name='product_name',
    title='Cost vs Sales Analysis'
)

st.plotly_chart(scatter_fig, use_container_width=True)

# Risk Table
st.subheader("🚨 Margin Risk Products")

risk_products = df[
    df['business_recommendation'] != 'Healthy Product'
]

st.dataframe(
    risk_products[[
        'product_name',
        'sales',
        'gross_margin_percent',
        'business_recommendation'
    ]]
)