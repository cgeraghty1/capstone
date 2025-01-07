from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd

app = Dash(__name__)
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
    html.Div([
        html.Label("Select Variables:"),
        dcc.Checklist(
            id="variable-selector",
            options=[{"label": col, "value": col} for col in fisher_data.columns[1:]],
            value=fisher_data.columns[1:]
        ),
        html.Div([
            html.Label("Adjust Weights for Each Variable:"),
            *[
                html.Div([
                    html.Label(col),
                    dcc.Slider(id=f"{col}-weight", min=0, max=5, step=0.1, value=1)
                ]) for col in fisher_data.columns[1:]
            ]
        ]),
    ]),
    dcc.Graph(id="fisher-chart")
])

@app.callback(
    Output("fisher-chart", "figure"),
    [
        Input("variable-selector", "value"),
        *[Input(f"{col}-weight", "value") for col in fisher_data.columns[1:]]
    ]
)
def update_chart(variables, *weights):
    selected_data = fisher_data[["Group"] + variables].copy()
    for i, col in enumerate(variables):
        selected_data[col] *= weights[i]

    fig = go.Figure()
    for col in variables:
        fig.add_trace(go.Bar(x=selected_data["Group"], y=selected_data[col], name=col))

    fig.update_layout(
        barmode="group",
        plot_bgcolor="white",
        xaxis=dict(title="Group"),
        yaxis=dict(title="Weighted Values")
    )
    return fig

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8080)
