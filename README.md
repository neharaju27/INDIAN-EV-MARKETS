# ⚡ Electric Vehicle Insights Dashboard

An interactive and responsive dashboard built with **Streamlit** and **Plotly** that provides a visual deep-dive into electric vehicle (EV) trends, categorized sales data, vehicle classes, and market performance over the years.

![EV Dashboard Banner](ev_market_logo.webp)

---

## 🎯 Motivation

With the rapid rise of electric vehicles, understanding the evolving landscape of EV adoption is crucial for manufacturers, policy makers, and consumers. This dashboard aims to:

- Provide a comprehensive overview of EV sales trends.
- Highlight key market players and their growth trajectories.
- Break down EV distribution by category and class.
- Offer insights into operational EV presence over time.

---

## 📊 Dashboard Walkthrough

Here's what you’ll find in the dashboard:

### 🔍 Filters Panel
- Toggle on/off to refine insights based on:
  - EV Maker
  - Year (2015–2024)
  - Vehicle Category (SUV, Sedan, etc.)
  - Vehicle Class

### 📈 KPIs and Visualizations
- **EV Sales Over Time:** Multi-year sales trend per maker.
- **Category Distribution:** Vehicle category performance for selected year.
- **Top EV Makers:** Ranking of top 10 makers by annual sales.
- **Vehicle Class Analysis:** Registration trends by class.
- **Market Share Pie Chart:** Proportional market share visualization.
- **YoY Growth Chart:** Percentage sales growth compared to the previous year.
- **EV Sales Trend (Line Chart):** Cumulative EV sales evolution over the years.
- **Data Explorer:** Tabular breakdown of filtered sales data.

---

## 🗂 Data Sources

The application processes and visualizes the following datasets (CSV files):
- `EV Maker by Place.csv`: EV makers by location.
- `ev_cat_01-24.csv`: Category-level EV data from 2001 to 2024.
- `ev_sales_by_makers_and_cat_15-24.csv`: Historical EV sales data by maker and category.
- `OperationalPC.csv`: Operational EV passenger cars data.
- `Vehicle Class - All.csv`: Data on EV registrations by vehicle class.

Ensure these files are placed in the project root.

---

## 🛠 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/ev-dashboard.git
   cd ev-dashboard
