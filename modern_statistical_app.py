import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd

app = dash.Dash(__name__)
app.title = "Modern Statistical Analysis Visualization"

modern_data = pd.DataFrame({
    "Group": ["White", "Black", "Asian", "Hispanic", "Other"],
    "IQ": [101, 98, 96, 95, 100],
    "Educational Attainment": [90, 75, 79, 70, 80],
    "Crime Statistics": [40, 39, 33, 40, 41],
    "Income Disparity": [70, 65, 85, 60, 65],
    "Health Outcomes": [80, 55, 75, 65, 70]
})

app.layout = html.Div([
    html.H1("Modern Statistical Analysis Visualization"),
    dcc.Graph(id="modern-chart"),
    html.Div([html.Label("Adjust Weights:"),
              dcc.Slider(id="weight-iq", min=0, max=5, value=1, marks={i: str(i) for i in range(6)})])
])

@app.callback(
    Output("modern-chart", "figure"),
    Input("weight-iq", "value")
)
def update_chart(weight_iq):
    data = modern_data.copy()
    data["IQ"] *= weight_iq
    fig = go.Figure(data=[go.Bar(x=data["Group"], y=data["IQ"], name="IQ")])
    return fig

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8080)
