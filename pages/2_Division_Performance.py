import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

# Load Data

df = pd.read_csv('final_nassau_data.csv')

st.title("🏭 Division Performance Dashboard")

# Revenue vs Profit

division_perf = df.groupby(
    'division'
).agg({
    'sales': 'sum',
    'gross_profit': 'sum'
}).reset_index()

fig = px.bar(
    division_perf,
    x='division',
    y=['sales', 'gross_profit'],
    barmode='group',
    title='Revenue vs Profit by Division'
)

st.plotly_chart(fig, use_container_width=True)

# Margin Distribution
st.subheader("📈 Margin Distribution")

margin_fig = px.box(
    df,
    x='division',
    y='gross_margin_percent',
    color='division',
    title='Margin Distribution by Division'
)

st.plotly_chart(margin_fig, use_container_width=True)

# Division Summary Table
st.subheader("📋 Division Summary")

summary = df.groupby('division').agg({
    'sales': 'sum',
    'gross_profit': 'sum',
    'gross_margin_percent': 'mean',
    'units': 'sum'
}).reset_index()

st.dataframe(summary)
