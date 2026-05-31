import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Nassau Candy Dashboard",
    page_icon="🍫",
    layout="wide"
)

# Load data
@st.cache_data

def load_data():
    df = pd.read_csv('final_nassau_data.csv')
    df['order_date'] = pd.to_datetime(df['order_date'])
    return df


df = load_data()

# Title
st.title("🍫 Nassau Candy Distributor Dashboard")
st.markdown("### Product Line Profitability & Margin Performance Analysis")

# Sidebar
st.sidebar.header("Dashboard Filters")

# Date Filter
start_date = st.sidebar.date_input(
    "Start Date",
    df['order_date'].min()
)
end_date = st.sidebar.date_input(
    "End Date",
    df['order_date'].max()
)

# Division Filter
selected_division = st.sidebar.multiselect(
    "Select Division",
    options=df['division'].unique(),
    default=df['division'].unique()
)

# Margin Slider
margin_threshold = st.sidebar.slider(
    "Minimum Gross Margin %",
    float(df['gross_margin_percent'].min()),
    float(df['gross_margin_percent'].max()),
    0.0
)

# Product Search
product_search = st.sidebar.text_input(
    "Search Product"
)
# Apply Filters
filtered_df = df[
    (df['division'].isin(selected_division)) &
    (df['gross_margin_percent'] >= margin_threshold)
]

filtered_df = filtered_df[
    (filtered_df['order_date'] >= pd.to_datetime(start_date)) &
    (filtered_df['order_date'] <= pd.to_datetime(end_date))
]
if product_search:
    filtered_df = filtered_df[
        filtered_df['product_name']
        .str.contains(product_search, case=False)
    ]

# KPI Calculations

total_sales = filtered_df['sales'].sum()
total_profit = filtered_df['gross_profit'].sum()
avg_margin = filtered_df['gross_margin_percent'].mean()
total_units = filtered_df['units'].sum()

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Sales",
    f"{total_sales:,.0f}"
)
col2.metric(
    "Total Profit",
    f"{total_profit:,.0f}"
)

col3.metric(
    "Average Margin %",
    f"{avg_margin:.2f}%"
)

col4.metric(
    "Total Units Sold",
    f"{total_units:,.0f}"
)

st.markdown("---")

# Sales Trend
st.subheader("📈 Monthly Sales Trend")

monthly_sales = filtered_df.groupby(
    filtered_df['order_date'].dt.to_period('M')
)['sales'].sum().reset_index()

monthly_sales['order_date'] = monthly_sales['order_date'].astype(str)

fig = px.line(
    monthly_sales,
    x='order_date',
    y='sales',
    title='Monthly Revenue Trend',
    markers=True
)
st.plotly_chart(fig, use_container_width=True)

# Executive Insights
st.subheader("🤖 Executive Insights")

best_product = filtered_df.groupby(
    'product_name'
)['gross_profit'].sum().idxmax()

best_profit = filtered_df.groupby(
    'product_name'
)['gross_profit'].sum().max()

st.info(
    f"Top profitable product is '{best_product}' generating ${best_profit:,.0f} gross profit."
)

st.success(
    "Chocolate division currently shows strongest financial performance."
)

st.warning(
    "Several high-sales products show weak margin efficiency and require pricing review."
)





# run app python -m streamlit run app.py
