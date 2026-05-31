import streamlit as st
import pandas as pd
import plotly.graph_objects as go
st.set_page_config(layout='wide')

# Load Data
df = pd.read_csv('final_nassau_data.csv')

st.title("📈 Profit Concentration Analysis")

# Pareto Data

pareto = df.groupby(
    'product_name'
)['gross_profit'].sum().reset_index()

pareto = pareto.sort_values(
    by='gross_profit',
    ascending=False
)

pareto['profit_contribution'] = (
    pareto['gross_profit'] /
    pareto['gross_profit'].sum()
) * 100

pareto['cumulative_profit'] = (
    pareto['profit_contribution']
).cumsum()

# Pareto Chart

fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=pareto['product_name'],
        y=pareto['gross_profit'],
        name='gross_profit'
    )
)

fig.add_trace(
    go.Scatter(
        x=pareto['product_name'],
        y=pareto['cumulative_profit'],
        name='Cumulative %',
        yaxis='y2'
    )
)

fig.update_layout(
    title='Pareto Analysis',
    yaxis2=dict(
        overlaying='y',
        side='right'
    )
)

st.plotly_chart(fig, use_container_width=True)

# Dependency Indicators
st.subheader("📌 Dependency Indicators")

high_dependency = pareto[
    pareto['cumulative_profit'] <= 80
]

st.dataframe(high_dependency)