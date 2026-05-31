import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

# Load Data

df = pd.read_csv('final_nassau_data.csv')

st.title("📄 Executive Summary")

# KPIs

total_sales = df['sales'].sum()
total_profit = df['gross_profit'].sum()
avg_margin = df['gross_margin_percent'].mean()

st.metric("Total Revenue", f"${total_sales:,.0f}")
st.metric("Total Profit", f"${total_profit:,.0f}")
st.metric("Average Margin", f"{avg_margin:.2f}%")

st.markdown("---")

st.subheader("Key Business Findings")

st.write("""
### Major Insights

- Chocolate division contributes highest profitability.
- Some products generate strong sales but weak margin efficiency.
- Margin concentration risk identified in limited product portfolio.
- Several products require repricing and cost renegotiation.
- Operational profitability varies significantly across divisions.
""")

st.subheader("Recommendations")

st.success("Increase focus on high-margin products.")
st.warning("Review low-margin high-sales products for pricing inefficiency.")
st.info("Reduce dependency on concentrated profit-driving products.")
