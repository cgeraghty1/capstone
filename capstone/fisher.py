import dash
from dash import dcc, html, Input, Output
import plotly.graph_objects as go
import pandas as pd
import numpy as np

app = dash.Dash(__name__)

# Generate random data for Ethnic Group
np.random.seed(42)
ethnic_data = pd.DataFrame({
    "Group": ["White", "Black", "Asian", "Hispanic", "Other"],
    "IQ": np.random.randint(80, 120, size=5),
    "Moral Character": np.random.randint(60, 100, size=5),
    "Violent Crime": np.random.randint(10, 50, size=5),
    "Income": np.random.randint(30, 100, size=5),
    "Reproduction Rate": np.random.randint(1, 5, size=5) * 10
})

# Generate random data for Environmental Impact
env_data = pd.DataFrame({
    "Country": ["A", "B", "C", "D", "E"],
    "CO2 Emissions": np.random.randint(10, 100, size=5),
    "GDP": np.random.randint(20, 80, size=5),
    "Renewable Energy": np.random.randint(10, 50, size=5),
    "Waste Generation": np.random.randint(20, 90, size=5),
    "Biodiversity Loss": np.random.randint(5, 30, size=5)
})

app.layout = html.Div([
    html.H1("Interactive Data Visualization: Ethnic Group and Environmental Data", style={"font-family": "Avenir", "text-align": "center"}),

    # Ethnic Group Data Visualization
    html.Div([
        html.H2("Interactive Data Visualization: Ethnic Group Data", style={"font-family": "Avenir"}),
        html.Div([
            html.Label("IQ Weight:", style={"font-family": "Avenir"}),
            dcc.Slider(id="iq-weight", min=0, max=3, step=0.1, value=1),
            html.Label("Moral Character Weight:", style={"font-family": "Avenir"}),
            dcc.Slider(id="moral-weight", min=0, max=3, step=0.1, value=1),
            html.Label("Violent Crime Weight:", style={"font-family": "Avenir"}),
            dcc.Slider(id="crime-weight", min=0, max=3, step=0.1, value=1),
            html.Label("Income Weight:", style={"font-family": "Avenir"}),
            dcc.Slider(id="income-weight", min=0, max=3, step=0.1, value=1),
            html.Label("Reproduction Rate Weight:", style={"font-family": "Avenir"}),
            dcc.Slider(id="reproduction-weight", min=0, max=3, step=0.1, value=1),
            html.Button("Reset Weights", id="reset-ethnic", n_clicks=0, style={"font-family": "Avenir", "margin-top": "10px"})
        ]),
        dcc.Graph(id="ethnic-graph")  # Only for Ethnic Group Data
    ], style={"margin-bottom": "50px"}),

    # Environmental Impact Data Visualization
    html.Div([
        html.H2("Interactive Data Visualization: Environmental Impact Data", style={"font-family": "Avenir"}),
        html.Div([
            html.Label("CO2 Emissions Weight:", style={"font-family": "Avenir"}),
            dcc.Slider(id="co2-weight", min=0, max=3, step=0.1, value=1),
            html.Label("GDP Weight:", style={"font-family": "Avenir"}),
            dcc.Slider(id="gdp-weight", min=0, max=3, step=0.1, value=1),
            html.Label("Renewable Energy Weight:", style={"font-family": "Avenir"}),
            dcc.Slider(id="renewable-weight", min=0, max=3, step=0.1, value=1),
            html.Label("Waste Generation Weight:", style={"font-family": "Avenir"}),
            dcc.Slider(id="waste-weight", min=0, max=3, step=0.1, value=1),
            html.Label("Biodiversity Loss Weight:", style={"font-family": "Avenir"}),
            dcc.Slider(id="biodiversity-weight", min=0, max=3, step=0.1, value=1),
            html.Button("Reset Weights", id="reset-env", n_clicks=0, style={"font-family": "Avenir", "margin-top": "10px"})
        ]),
        dcc.Graph(id="env-graph")  # Only for Environmental Impact Data
    ])
])

# Callback for Ethnic Group Visualization
@app.callback(
    Output("ethnic-graph", "figure"),
    [Input("iq-weight", "value"),
     Input("moral-weight", "value"),
     Input("crime-weight", "value"),
     Input("income-weight", "value"),
     Input("reproduction-weight", "value"),
     Input("reset-ethnic", "n_clicks")]
)
def update_ethnic_graph(iq_w, moral_w, crime_w, income_w, reproduction_w, reset):
    weights = [iq_w, moral_w, crime_w, income_w, reproduction_w]
    if reset > 0:
        weights = [1, 1, 1, 1, 1]
    weighted_data = ethnic_data.copy()
    for i, col in enumerate(["IQ", "Moral Character", "Violent Crime", "Income", "Reproduction Rate"]):
        weighted_data[col] *= weights[i]
    fig = go.Figure()
    for col in ["IQ", "Moral Character", "Violent Crime", "Income", "Reproduction Rate"]:
        fig.add_trace(go.Bar(x=weighted_data["Group"], y=weighted_data[col], name=col, opacity=0.75))
    fig.update_layout(title="Weighted Ethnic Group Data", barmode="group", plot_bgcolor="white", font_family="Avenir")
    return fig

# Callback for Environmental Impact Visualization
@app.callback(
    Output("env-graph", "figure"),
    [Input("co2-weight", "value"),
     Input("gdp-weight", "value"),
     Input("renewable-weight", "value"),
     Input("waste-weight", "value"),
     Input("biodiversity-weight", "value"),
     Input("reset-env", "n_clicks")]
)
def update_env_graph(co2_w, gdp_w, renewable_w, waste_w, biodiversity_w, reset):
    weights = [co2_w, gdp_w, renewable_w, waste_w, biodiversity_w]
    if reset > 0:
        weights = [1, 1, 1, 1, 1]
    weighted_data = env_data.copy()
    for i, col in enumerate(["CO2 Emissions", "GDP", "Renewable Energy", "Waste Generation", "Biodiversity Loss"]):
        weighted_data[col] *= weights[i]
    fig = go.Figure()
    for col in ["CO2 Emissions", "GDP", "Renewable Energy", "Waste Generation", "Biodiversity Loss"]:
        fig.add_trace(go.Bar(x=weighted_data["Country"], y=weighted_data[col], name=col, opacity=0.75))
    fig.update_layout(title="Weighted Environmental Impact Data", barmode="group", plot_bgcolor="white", font_family="Avenir")
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
