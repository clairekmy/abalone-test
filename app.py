import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px
import streamlit as st

# Access the dataset path from Streamlit secrets
dataset_path = st.secrets["datasets"]["abalone_path"]

# Define column names
columns = [
    "Sex", "Length", "Diameter", "Height", "WholeWeight", 
    "ShuckedWeight", "VisceraWeight", "ShellWeight", "Rings"
]

# Load the dataset
df = pd.read_csv(dataset_path, header=None, names=columns)

# Initialize the Dash app
app = Dash(__name__)

# Scatter Plot
fig1 = px.scatter(
    df,
    x="Rings",
    y="Length",
    color="Sex",
    title="Scatter Plot of Rings vs. Length",
    labels={"Rings": "Age (Rings)", "Length": "Length (mm)"},
)

# Histogram
fig2 = px.histogram(
    df,
    x="Rings",
    nbins=20,
    color="Sex",
    title="Histogram of Rings by Sex",
    labels={"Rings": "Age (Rings)"},
)

# Box Plot
fig3 = px.box(
    df,
    x="Sex",
    y="Length",
    color="Sex",
    title="Box Plot of Length by Sex",
    labels={"Sex": "Sex", "Length": "Length (mm)"},
)

# Bar Chart
avg_weights = df.groupby("Sex")[["WholeWeight"]].mean().reset_index()
fig4 = px.bar(
    avg_weights,
    x="Sex",
    y="WholeWeight",
    color="Sex",
    title="Average Whole Weight by Sex",
    labels={"Sex": "Sex", "WholeWeight": "Average Weight (g)"},
)

# Layout for the Dash app
app.layout = html.Div([
    html.H1("Abalone Dataset Dashboard"),
    
    html.Div([
        html.H2("Scatter Plot"),
        dcc.Graph(id="scatter-plot", figure=fig1)
    ]),

    html.Div([
        html.H2("Histogram"),
        dcc.Graph(id="histogram", figure=fig2)
    ]),

    html.Div([
        html.H2("Box Plot"),
        dcc.Graph(id="box-plot", figure=fig3)
    ]),

    html.Div([
        html.H2("Bar Chart"),
        dcc.Graph(id="bar-chart", figure=fig4)
    ]),
])

# Run the app
if __name__ == "__main__":
    app.run_server(debug=False)
