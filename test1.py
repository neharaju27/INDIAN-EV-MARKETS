import streamlit as st
import pandas as pd
import plotly.express as px

# Load datasets
def load_data():
    ev_maker_data = pd.read_csv('EV Maker by Place.csv')
    ev_category_data = pd.read_csv('ev_cat_01-24.csv')
    ev_sales_data = pd.read_csv('ev_sales_by_makers_and_cat_15-24.csv')
    operational_pc_data = pd.read_csv('OperationalPC.csv')
    vehicle_class_data = pd.read_csv('Vehicle Class - All.csv')
    return ev_maker_data, ev_category_data, ev_sales_data, operational_pc_data, vehicle_class_data

# Load data
ev_maker_data, ev_category_data, ev_sales_data, operational_pc_data, vehicle_class_data = load_data()

# Standardize column names
ev_sales_data.columns = ev_sales_data.columns.str.strip().str.lower()
ev_category_data.columns = ev_category_data.columns.str.strip().str.lower()
vehicle_class_data.columns = vehicle_class_data.columns.str.strip().str.lower()

# Reshape sales data from wide to long format
ev_sales_data_melted = ev_sales_data.melt(id_vars=['maker', 'cat'],
                                          var_name='year',
                                          value_name='sales')
ev_sales_data_melted['year'] = ev_sales_data_melted['year'].astype(int)

# Streamlit App
st.set_page_config(page_title="EV Data Explorer", layout="wide")

# Sidebar Toggle
if 'show_filters' not in st.session_state:
    st.session_state['show_filters'] = False

def toggle_filters():
    st.session_state['show_filters'] = not st.session_state['show_filters']

# Logo as button to toggle filters
st.sidebar.image("ev market logo.webp", width=200)
if st.sidebar.button("🔍 Click Logo to Show/Hide Filters"):
    toggle_filters()

if st.session_state['show_filters']:
    st.sidebar.header("Filter Options")
    selected_maker = st.sidebar.selectbox("Select EV Maker", ['All'] + list(ev_sales_data_melted['maker'].unique()))
    selected_year = st.sidebar.slider("Select Year", int(ev_sales_data_melted['year'].min()), int(ev_sales_data_melted['year'].max()), int(ev_sales_data_melted['year'].max()))
    selected_category = st.sidebar.selectbox("Select Vehicle Category", ['All'] + list(ev_sales_data_melted['cat'].unique()))
    selected_vehicle_class = st.sidebar.selectbox("Select Vehicle Class", ['All'] + list(vehicle_class_data['vehicle class'].unique()))

# Main Title
st.title("🔋 Electric Vehicle Insights Dashboard")
st.markdown("Explore trends, sales, and insights in the EV market with interactive visualizations.")

# Set default value for selected_year in case no filter is applied
selected_year = selected_year if st.session_state['show_filters'] else int(ev_sales_data_melted['year'].max())

# Apply filters
filtered_sales = ev_sales_data_melted[ev_sales_data_melted['year'] == selected_year]
if st.session_state['show_filters'] and selected_maker != 'All':
    filtered_sales = filtered_sales[filtered_sales['maker'] == selected_maker]
if st.session_state['show_filters'] and selected_category != 'All':
    filtered_sales = filtered_sales[filtered_sales['cat'] == selected_category]

filtered_vehicle_class = vehicle_class_data.copy()
if st.session_state['show_filters'] and selected_vehicle_class != 'All':
    filtered_vehicle_class = filtered_vehicle_class[filtered_vehicle_class['vehicle class'] == selected_vehicle_class]

# KPI 1: EV Sales Over Time
st.subheader("📈 EV Sales Over Time")
fig1 = px.bar(filtered_sales, x='year', y='sales', color='maker', title=f"EV Sales Over Time")
st.plotly_chart(fig1, use_container_width=True)

# KPI 2: Sales Distribution by Category for Selected Year
st.subheader(f"📊 Sales Distribution by Vehicle Category in {selected_year}")
fig2 = px.bar(filtered_sales, x='cat', y='sales', title=f"EV Sales Distribution in {selected_year}")
st.plotly_chart(fig2, use_container_width=True)

# KPI 3: Top 10 EV Makers by Sales in Selected Year
st.subheader(f"🏆 Top 10 EV Makers by Sales in {selected_year}")
top_makers = filtered_sales.groupby('maker')['sales'].sum().nlargest(10).reset_index()
fig3 = px.bar(top_makers, x='maker', y='sales', title=f"Top 10 EV Makers in {selected_year}")
st.plotly_chart(fig3, use_container_width=True)

# KPI 4: Vehicle Class Distribution
st.subheader("🚗 EV Vehicle Class Distribution")
fig4 = px.bar(filtered_vehicle_class, x='vehicle class', y='total registration', title="Distribution of EV Vehicle Classes")
st.plotly_chart(fig4, use_container_width=True)

# KPI 5: Yearly Sales Trend for All Makers
st.subheader("📊 Yearly Sales Trend for All EV Makers")
fig5 = px.bar(ev_sales_data_melted.groupby(['year', 'maker'])['sales'].sum().reset_index(), x='year', y='sales', color='maker', title="Yearly Sales Trend for All EV Makers")
st.plotly_chart(fig5, use_container_width=True)

# KPI 6: EV Market Share by Maker in Selected Year
st.subheader(f"📌 EV Market Share by Maker in {selected_year}")
market_share = filtered_sales.groupby('maker')['sales'].sum().reset_index()
fig6 = px.pie(market_share, names='maker', values='sales', title=f"Market Share of EV Makers in {selected_year}")
st.plotly_chart(fig6, use_container_width=True)

# KPI 7: Growth in Sales Compared to Previous Year
st.subheader("📈 Year-over-Year Sales Growth")
ev_sales_data_melted['prev_year_sales'] = ev_sales_data_melted.groupby(['maker', 'cat'])['sales'].shift(1)
ev_sales_data_melted['growth'] = ((ev_sales_data_melted['sales'] - ev_sales_data_melted['prev_year_sales']) / ev_sales_data_melted['prev_year_sales']) * 100
fig7 = px.bar(ev_sales_data_melted.dropna(), x='year', y='growth', color='maker', title="Year-over-Year Sales Growth")
st.plotly_chart(fig7, use_container_width=True)

# KPI 8: Line Chart for EV Sales Trend
st.subheader("📉 EV Sales Trend Over Years")
fig8 = px.line(ev_sales_data_melted.groupby('year')['sales'].sum().reset_index(), x='year', y='sales', title="EV Sales Trend Over Years", markers=True)
st.plotly_chart(fig8, use_container_width=True)

# Additional insights
st.markdown("### 🔎 Explore the Data")
st.dataframe(filtered_sales)
