import streamlit as st
import pandas as pd

# Page setup for the interface
st.set_page_config(layout="wide")
st.title("🧬 Stem Cell Translation & Enterprise Database")
st.write("An interactive repository built to analyze the operational bottlenecks and scale-up solutions for advanced therapies.")

# Load data
df = pd.read_csv("stem_cells.csv")

# Create user selection filter sidebar
selected_cell = st.sidebar.selectbox("Query Cell Type:", df['Cell_Type'].unique())

# Filter data dynamically based on selection
display_data = df[df['Cell_Type'] == selected_cell]

# Render the formatted database on the user interface
st.subheader(f"Strategic Profile: {selected_cell}")
st.dataframe(display_data, use_container_width=True)