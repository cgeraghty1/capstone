import dash
from dash import dcc, html
import plotly.graph_objects as go
import pandas as pd

# Initialize the Dash app
app = dash.Dash(__name__)
app.title = "Interactive Visualizations"

# Generate Random Data for Ethnic Group Visualization
ethnic_data = pd.DataFrame({
    "Group": ["White", "Black", "Asian", "Hispanic", "Other"],
    "IQ": [110, 90, 105, 95, 100],
    "Moral Character": [95, 85, 90, 80, 85],
    "Violent Crime": [10, 50, 15, 40, 30],
    "Income": [75, 45, 70, 50, 55],
    "Reproduction Rate": [48, 55, 47, 60, 52]
})

# Generate Random Data for Environmental Impact Visualization
env_data = pd.DataFrame({
    "Country": ["A", "B", "C", "D", "E"],
    "CO2 Emissions": [50, 20, 40, 70, 30],
    "GDP": [60, 30, 55, 20, 40],
    "Renewable Energy": [15, 50, 20, 10, 30],
    "Waste Generation": [80, 40, 70, 100, 50],
    "Biodiversity Loss": [35, 60, 45, 70, 50]
})

# Ethnic Group Visualization
ethnic_fig = go.Figure()
for col in ["IQ", "Moral Character", "Violent Crime", "Income", "Reproduction Rate"]:
    ethnic_fig.add_trace(go.Bar(x=ethnic_data["Group"], y=ethnic_data[col], name=col, opacity=0.75))
ethnic_fig.update_layout(title="Interactive Data Visualization: Ethnic Group Data",
                         barmode="group", plot_bgcolor="white", font_family="Avenir")

# Environmental Impact Visualization
env_fig = go.Figure()
for col in ["CO2 Emissions", "GDP", "Renewable Energy", "Waste Generation", "Biodiversity Loss"]:
    env_fig.add_trace(go.Bar(x=env_data["Country"], y=env_data[col], name=col, opacity=0.75))
env_fig.update_layout(title="Interactive Data Visualization: Environmental Impact Data",
                      barmode="group", plot_bgcolor="white", font_family="Avenir")

# Layout for Dash Application
app.layout = html.Div([
    html.Header([
        html.H1("Interactive Visualizations"),
        html.P("Explore and interact with the data visualizations below.")
    ]),

    # Ethnic Group Data Visualization
    html.Section([
        html.H2("Ethnic Group Data"),
        dcc.Graph(figure=ethnic_fig)
    ]),

    # Environmental Impact Data Visualization
    html.Section([
        html.H2("Environmental Impact Data"),
        dcc.Graph(figure=env_fig)
    ]),

    html.Footer([
        html.P("© 2024 Colin Geraghty. All rights reserved.")
    ])
])

# Run the Dash server
if __name__ == "__main__":
    app.run_server(debug=True)
