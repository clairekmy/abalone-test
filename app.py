import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load the Abalone dataset and assign column names
columns = [
    "Sex", "Length", "Diameter", "Height", "WholeWeight", 
    "ShuckedWeight", "VisceraWeight", "ShellWeight", "Rings"
]
df = pd.read_csv('abalone.data', header=None, names=columns)

# Initialize Dash app
app = dash.Dash(__name__)

# Create a scatter plot using Plotly Express
fig = px.scatter(
    df,
    x="Rings",  # Replace with a column name from the dataset
    y="Length",  # Replace with another column name from the dataset
    color="Sex",  # Replace with a categorical column (if available)
    title="Abalone Dataset Visualization",
    labels={"Rings": "Age Rings", "Length": "Shell Length"},
)

# Define the layout of the Dash app
app.layout = html.Div([
    html.H1("Abalone Dataset Dashboard"),
    dcc.Graph(id="abalone-scatter-plot", figure=fig)
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug= False)


