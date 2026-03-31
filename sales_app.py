import streamlit as st
import pandas as pd

# App title and description
st.title("📊 Sales Summary Dashboard")
st.subheader("Interactive view of product sales by category")

# Hardcoded dataset
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Headphones", "Smartwatch"],
    "Category": ["Electronics", "Electronics", "Electronics", "Accessories", "Accessories"],
    "Sales": [1500, 800, 600, 200, 300]
}

df = pd.DataFrame(data)

# Sidebar filter
st.sidebar.header("Filter Options")
selected_category = st.sidebar.selectbox(
    "Select Category",
    df["Category"].unique()
)

# Filter dataframe
filtered_df = df[df["Category"] == selected_category]

# Display filtered data
st.write(f"### Showing data for: {selected_category}")
st.dataframe(filtered_df)

# Line chart of sales
st.write("### Sales Trend")
st.line_chart(filtered_df["Sales"])