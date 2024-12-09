import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "Modern Statistical Analysis Visualization"

# Data for the visualization
modern_data = pd.DataFrame({
    "Group": ["White", "Black", "Asian", "Hispanic", "Other"],
    "IQ": [101, 98, 96, 95, 100],
    "Educational Attainment": [90, 75, 79, 70, 80],
    "Crime Statistics": [40, 39, 33, 40, 41],
    "Income Disparity": [70, 65, 85, 60, 65],
    "Health Outcomes": [80, 55, 75, 65, 70]
})

# App layout
app.layout = html.Div([
    html.H1("Modern Statistical Analysis Visualization"),
    dcc.Graph(id="stat-chart"),
    html.Div([
        html.Label("Adjust Weights:"),
        html.Div([
            html.Label("IQ"),
            dcc.Slider(id="weight-iq", min=0, max=5, step=0.1, value=1, marks={i: str(i) for i in range(6)}),
        ]),
        html.Div([
            html.Label("Educational Attainment"),
            dcc.Slider(id="weight-education", min=0, max=5, step=0.1, value=1, marks={i: str(i) for i in range(6)}),
        ]),
        html.Div([
            html.Label("Crime Statistics"),
            dcc.Slider(id="weight-crime", min=0, max=5, step=0.1, value=1, marks={i: str(i) for i in range(6)}),
        ]),
        html.Div([
            html.Label("Income Disparity"),
            dcc.Slider(id="weight-income", min=0, max=5, step=0.1, value=1, marks={i: str(i) for i in range(6)}),
        ]),
        html.Div([
            html.Label("Health Outcomes"),
            dcc.Slider(id="weight-health", min=0, max=5, step=0.1, value=1, marks={i: str(i) for i in range(6)}),
        ]),
    ], style={"margin-top": "20px"}),
])

# Callback to update chart based on weights
@app.callback(
    Output("stat-chart", "figure"),
    [Input("weight-iq", "value"),
     Input("weight-education", "value"),
     Input("weight-crime", "value"),
     Input("weight-income", "value"),
     Input("weight-health", "value")]
)
def update_chart(weight_iq, weight_education, weight_crime, weight_income, weight_health):
    # Apply weights to data
    weighted_data = modern_data.copy()
    weighted_data["IQ"] *= weight_iq
    weighted_data["Educational Attainment"] *= weight_education
    weighted_data["Crime Statistics"] *= weight_crime
    weighted_data["Income Disparity"] *= weight_income
    weighted_data["Health Outcomes"] *= weight_health

    # Create the bar chart
    fig = go.Figure()
    for col, color in zip(
        ["IQ", "Educational Attainment", "Crime Statistics", "Income Disparity", "Health Outcomes"],
        ["#636EFA", "#EF553B", "#00CC96", "#AB63FA", "#FFA15A"]
    ):
        fig.add_trace(go.Bar(x=weighted_data["Group"], y=weighted_data[col], name=col, marker=dict(color=color)))

    # Update layout for clarity
    fig.update_layout(
        barmode="group",
        title="Weighted Statistical Values by Group",
        xaxis_title="Group",
        yaxis_title="Weighted Values",
        plot_bgcolor="white",
        legend_title="Variables"
    )
    return fig

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8080)
