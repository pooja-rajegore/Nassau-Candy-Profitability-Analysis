import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

# Load Data
df = pd.read_csv('final_nassau_data.csv')

st.title("🏆 Product Profitability Overview")

# =========================
# TOP PRODUCTS
# =========================

product_profit = (
    df.groupby('product_name')['gross_profit']
    .sum()
    .reset_index()
)

product_profit = product_profit.sort_values(
    by='gross_profit',
    ascending=False
).head(15)

fig = px.bar(
    product_profit,
    x='gross_profit',
    y='product_name',
    orientation='h',
    color='gross_profit',
    title='Top Products by Gross Profit'
)

fig.update_layout(
    yaxis={'categoryorder':'total ascending'}
)

st.plotly_chart(fig, use_container_width=True)

# =========================
# LEADERBOARD
# =========================

st.subheader("📊 Product Margin Leaderboard")

leaderboard = (
    df.groupby('product_name')
    .agg({
        'gross_margin_percent': 'mean',
        'gross_profit': 'sum',
        'sales': 'sum'
    })
    .reset_index()
)

leaderboard = leaderboard.sort_values(
    by='gross_margin_percent',
    ascending=False
)

# Rounding
leaderboard['gross_margin_percent'] = (
    leaderboard['gross_margin_percent']
    .round(2)
)

leaderboard['gross_profit'] = (
    leaderboard['gross_profit']
    .round(2)
)

leaderboard['sales'] = (
    leaderboard['sales']
    .round(2)
)

st.dataframe(leaderboard)

# =========================
# PIE CHART
# =========================

st.subheader("🥧 Profit Contribution Analysis")

profit_contribution = (
    df.groupby('division')['gross_profit']
    .sum()
    .reset_index()
)

pie_fig = px.pie(
    profit_contribution,
    names='division',
    values='gross_profit',
    title='Profit Contribution by Division',
    color_discrete_sequence=px.colors.sequential.RdBu
)

st.plotly_chart(
    pie_fig,
    use_container_width=True
)
print(df.columns)
