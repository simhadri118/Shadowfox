# ==============================
# SALES DASHBOARD + ML (FINAL FIXED)
# ==============================

import streamlit as st
import pandas as pd
import plotly.express as px

# ML Libraries
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error

# ------------------------------
# PAGE CONFIG
# ------------------------------
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# ------------------------------
#  UI STYLE
# ------------------------------
st.markdown("""
<style>
.main-title {
    font-size: 40px;
    font-weight: bold;
    color: #4CAF50;
}
.card {
    background-color: #1E1E1E;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title"> SALES </p>', unsafe_allow_html=True)

# ------------------------------
# LOAD DATA
# ------------------------------
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("sales.csv")
    except:
        st.error(" sales.csv file not found")
        st.stop()

    df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True, errors="coerce")
    df = df.dropna(subset=["Order Date"])

    return df

data = load_data()

# ------------------------------
#  ML MODEL (FIXED)
# ------------------------------
@st.cache_resource
def train_model(data):

    df = data.copy()

    # Feature Engineering
    df["Month"] = df["Order Date"].dt.month
    df["Year"] = df["Order Date"].dt.year

    # Remove text column causing error
    df = df.drop(columns=["Product Name"], errors="ignore")

    # Encode categorical
    df = pd.get_dummies(df, columns=["Region", "Category"], drop_first=True)

    # Features & Target
    X = df.drop(["Sales", "Order Date"], axis=1, errors="ignore")
    y = df["Sales"]

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Model
    model = RandomForestRegressor(n_estimators=150, random_state=42)
    model.fit(X_train, y_train)

    # Evaluation
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)

    return model, X.columns, r2, mae


model, feature_columns, r2, mae = train_model(data)

# ------------------------------
# SIDEBAR FILTERS
# ------------------------------
st.sidebar.title(" Filters")

region = st.sidebar.multiselect(
    "Region", data["Region"].unique(), default=data["Region"].unique()
)

category = st.sidebar.multiselect(
    "Category", data["Category"].unique(), default=data["Category"].unique()
)

# Date filter
min_date = data["Order Date"].min().date()
max_date = data["Order Date"].max().date()

date_range = st.sidebar.date_input("Date Range", (min_date, max_date))

if len(date_range) != 2:
    st.warning("Please select a valid date range")
    st.stop()

start_date, end_date = date_range

# Apply filter
filtered_data = data[
    (data["Region"].isin(region)) &
    (data["Category"].isin(category)) &
    (data["Order Date"].dt.date >= start_date) &
    (data["Order Date"].dt.date <= end_date)
]

if filtered_data.empty:
    st.warning("Please select a valid date range")
    st.stop()

# ------------------------------
# KPI CARDS
# ------------------------------
sales = filtered_data["Sales"].sum()
profit = filtered_data["Profit"].sum()
orders = filtered_data.shape[0]

c1, c2, c3 = st.columns(3)

c1.markdown(f'<div class="card"><h3> Sales</h3><h2>{sales:,.0f}</h2></div>', unsafe_allow_html=True)
c2.markdown(f'<div class="card"><h3> Profit</h3><h2>{profit:,.0f}</h2></div>', unsafe_allow_html=True)
c3.markdown(f'<div class="card"><h3> Orders</h3><h2>{orders}</h2></div>', unsafe_allow_html=True)

st.markdown("---")

# ------------------------------
# MODEL PERFORMANCE
# ------------------------------
st.subheader(" Model Performance")

m1, m2 = st.columns(2)
m1.metric("R² Score", f"{r2:.2f}")
m2.metric("MAE", f"{mae:.2f}")

# ------------------------------
# CHARTS
# ------------------------------
col1, col2 = st.columns(2)

with col1:
    fig = px.bar(filtered_data, x="Region", y="Sales", color="Region", title="Sales by Region")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.bar(filtered_data, x="Category", y="Sales", color="Category", title="Sales by Category")
    st.plotly_chart(fig, use_container_width=True)

# Trend
filtered_data = filtered_data.copy()
filtered_data["Month"] = filtered_data["Order Date"].dt.to_period("M").astype(str)

fig = px.line(filtered_data, x="Month", y="Sales", title="Monthly Trend", markers=True)
st.plotly_chart(fig, use_container_width=True)

# Scatter
if "Discount" in filtered_data.columns:
    fig = px.scatter(filtered_data, x="Discount", y="Profit", color="Category", title="Discount vs Profit")
    st.plotly_chart(fig, use_container_width=True)

# Pie
fig = px.pie(filtered_data, names="Category", values="Sales", title="Category Distribution")
st.plotly_chart(fig, use_container_width=True)

# Heatmap
numeric = filtered_data.select_dtypes(include="number")
if not numeric.empty:
    fig = px.imshow(numeric.corr(), text_auto=True, title="Correlation Heatmap")
    st.plotly_chart(fig, use_container_width=True)

# ------------------------------
#  PREDICTION
# ------------------------------
st.markdown("---")
st.subheader(" Predict Sales")

col1, col2 = st.columns(2)

with col1:
    input_profit = st.number_input("Profit", value=100.0)
    input_discount = st.number_input("Discount", value=0.1)

with col2:
    input_region = st.selectbox("Region", data["Region"].unique())
    input_category = st.selectbox("Category", data["Category"].unique())

input_month = st.selectbox("Month", list(range(1, 13)))
input_year = st.selectbox("Year", sorted(data["Order Date"].dt.year.unique()))

input_df = pd.DataFrame({
    "Profit": [input_profit],
    "Discount": [input_discount],
    "Month": [input_month],
    "Year": [input_year],
    "Region": [input_region],
    "Category": [input_category]
})

input_encoded = pd.get_dummies(input_df)
input_encoded = input_encoded.reindex(columns=feature_columns, fill_value=0)

prediction = model.predict(input_encoded)

st.success(f" Predicted Sales: {prediction[0]:,.2f}")

# ------------------------------
# DOWNLOAD
# ------------------------------
st.download_button(
    "Download CSV",
    filtered_data.to_csv(index=False),
    "filtered_data.csv",
    "text/csv"
)
if st.checkbox("Show Data"):
    st.dataframe(data)