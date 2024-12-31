import pandas as pd
import streamlit as st
import plotly.express as px

# Access the dataset path from Streamlit secrets
dataset_path = st.secrets["datasets"]["abalone_path"]

# Load the dataset
columns = [
    "Sex", "Length", "Diameter", "Height", "WholeWeight", 
    "ShuckedWeight", "VisceraWeight", "ShellWeight", "Rings"
]
df = pd.read_csv(dataset_path, header=None, names=columns)

# Streamlit UI
st.title("Abalone Dataset Visualization")

# Scatter plot using Plotly
fig = px.scatter(
    df,
    x="Rings",  # Age proxy
    y="Length",  # Feature to visualize
    color="Sex",  # Grouping by categorical variable
    title="Abalone Dataset Visualization",
    labels={"Rings": "Age (Rings)", "Length": "Length (mm)"},
)
st.plotly_chart(fig)
