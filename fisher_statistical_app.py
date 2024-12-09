import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd

app = dash.Dash(__name__)
app.title = "Fisher Statistical Visualization"

fisher_data = pd.DataFrame({
    "Group": ["White", "Black", "Asian", "Hispanic", "Other"],
    "IQ": [100, 108, 105, 102, 98],
    "Moral Character": [95, 85, 90, 80, 85],
    "Violent Crime": [30, 35, 25, 40, 45],
    "Income": [75, 45, 70, 50, 55],
    "Reproduction Rate": [48, 55, 47, 60, 52]
})

app.layout = html.Div([
    html.H1("Fisher Statistical Visualization"),
    dcc.Graph(id="stat-chart"),
    html.Div([
        html.Label("Adjust Weights:"),
        dcc.Slider(id="weight-iq", min=0, max=5, value=1, marks={i: str(i) for i in range(6)}),
        dcc.Slider(id="weight-moral", min=0, max=5, value=1, marks={i: str(i) for i in range(6)}),
        dcc.Slider(id="weight-crime", min=0, max=5, value=1, marks={i: str(i) for i in range(6)}),
        dcc.Slider(id="weight-income", min=0, max=5, value=1, marks={i: str(i) for i in range(6)}),
        dcc.Slider(id="weight-reproduction", min=0, max=5, value=1, marks={i: str(i) for i in range(6)})
    ])
])

@app.callback(
    Output("stat-chart", "figure"),
    [Input("weight-iq", "value"),
     Input("weight-moral", "value"),
     Input("weight-crime", "value"),
     Input("weight-income", "value"),
     Input("weight-reproduction", "value")]
)
def update_chart(weight_iq, weight_moral, weight_crime, weight_income, weight_reproduction):
    weighted_data = fisher_data.copy()
    weighted_data["IQ"] *= weight_iq
    weighted_data["Moral Character"] *= weight_moral
    weighted_data["Violent Crime"] *= weight_crime
    weighted_data["Income"] *= weight_income
    weighted_data["Reproduction Rate"] *= weight_reproduction

    fig = go.Figure()
    for col, color in zip(
        ["IQ", "Moral Character", "Violent Crime", "Income", "Reproduction Rate"],
        ["#636EFA", "#EF553B", "#00CC96", "#AB63FA", "#FFA15A"]
    ):
        fig.add_trace(go.Bar(x=weighted_data["Group"], y=weighted_data[col], name=col, marker=dict(color=color)))
    fig.update_layout(barmode="group", title="Weighted Statistical Values")
    return fig

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8080)
