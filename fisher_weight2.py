import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "Modern Statistical Analysis Visualization"

# Generate random data with the new variables
modern_data = pd.DataFrame({
    "Group": ["White", "Black", "Asian", "Hispanic", "Other"],
    "IQ": [101, 98, 96, 95, 100],
    "Educational Attainment": [90, 75, 79, 70, 80],
    "Crime Statistics": [40, 39, 33, 40, 41],
    "Income Disparity": [70, 65, 85, 60, 65],
    "Health Outcomes": [80, 55, 75, 65, 70]
})

# App layout
app.layout = html.Div(style={"font-family": "Avenir", "padding": "10px", "max-width": "1000px", "margin": "0 auto", "font-size": "0.95em"}, children=[
    # Clickable variable titles for toggling visibility
    html.Div(
        style={"display": "flex", "justify-content": "center", "gap": "8px", "margin-bottom": "10px"},
        children=[
            html.Div("IQ", id="toggle-iq", style={"color": "#636EFA", "font-weight": "bold", "cursor": "pointer"}),
            html.Div("Educational Attainment", id="toggle-education", style={"color": "#EF553B", "font-weight": "bold", "cursor": "pointer"}),
            html.Div("Crime Statistics", id="toggle-crime", style={"color": "#00CC96", "font-weight": "bold", "cursor": "pointer"}),
            html.Div("Income Disparity", id="toggle-income", style={"color": "#AB63FA", "font-weight": "bold", "cursor": "pointer"}),
            html.Div("Health Outcomes", id="toggle-health", style={"color": "#FFA15A", "font-weight": "bold", "cursor": "pointer"})
        ]
    ),

    # Bar Chart
    dcc.Graph(id="modern-chart", style={"width": "100%", "height": "400px", "border": "none"}),

    # Sliders with corresponding value display
    html.Div(
        style={"display": "flex", "justify-content": "space-around", "align-items": "center", "margin-top": "10px"},
        children=[
            html.Div([
                html.Label("IQ", style={"font-weight": "bold", "font-size": "0.85em", "text-align": "center"}),
                dcc.Slider(
                    id="weight-iq",
                    min=0,
                    max=5,
                    step=0.1,
                    value=1,
                    marks={i: str(round(i, 1)) for i in [0, 1, 2, 3, 4, 5]}
                ),
                html.Div(id="weight-iq-value", style={"text-align": "center", "font-size": "0.85em", "margin-top": "-10px"})
            ], style={"width": "18%"}),
            html.Div([
                html.Label("Educational Attainment", style={"font-weight": "bold", "font-size": "0.85em", "text-align": "center"}),
                dcc.Slider(
                    id="weight-education",
                    min=0,
                    max=5,
                    step=0.1,
                    value=1,
                    marks={i: str(round(i, 1)) for i in [0, 1, 2, 3, 4, 5]}
                ),
                html.Div(id="weight-education-value", style={"text-align": "center", "font-size": "0.85em", "margin-top": "-10px"})
            ], style={"width": "18%"}),
            html.Div([
                html.Label("Crime Statistics", style={"font-weight": "bold", "font-size": "0.85em", "text-align": "center"}),
                dcc.Slider(
                    id="weight-crime",
                    min=0,
                    max=5,
                    step=0.1,
                    value=1,
                    marks={i: str(round(i, 1)) for i in [0, 1, 2, 3, 4, 5]}
                ),
                html.Div(id="weight-crime-value", style={"text-align": "center", "font-size": "0.85em", "margin-top": "-10px"})
            ], style={"width": "18%"}),
            html.Div([
                html.Label("Income Disparity", style={"font-weight": "bold", "font-size": "0.85em", "text-align": "center"}),
                dcc.Slider(
                    id="weight-income",
                    min=0,
                    max=5,
                    step=0.1,
                    value=1,
                    marks={i: str(round(i, 1)) for i in [0, 1, 2, 3, 4, 5]}
                ),
                html.Div(id="weight-income-value", style={"text-align": "center", "font-size": "0.85em", "margin-top": "-10px"})
            ], style={"width": "18%"}),
            html.Div([
                html.Label("Health Outcomes", style={"font-weight": "bold", "font-size": "0.85em", "text-align": "center"}),
                dcc.Slider(
                    id="weight-health",
                    min=0,
                    max=5,
                    step=0.1,
                    value=1,
                    marks={i: str(round(i, 1)) for i in [0, 1, 2, 3, 4, 5]}
                ),
                html.Div(id="weight-health-value", style={"text-align": "center", "font-size": "0.85em", "margin-top": "-10px"})
            ], style={"width": "18%"})
        ]
    )
])

# Callback to update chart and toggle visibility
@app.callback(
    Output("modern-chart", "figure"),
    [Input("weight-iq", "value"),
     Input("weight-education", "value"),
     Input("weight-crime", "value"),
     Input("weight-income", "value"),
     Input("weight-health", "value"),
     Input("toggle-iq", "n_clicks"),
     Input("toggle-education", "n_clicks"),
     Input("toggle-crime", "n_clicks"),
     Input("toggle-income", "n_clicks"),
     Input("toggle-health", "n_clicks")]
)
def update_modern_chart(weight_iq, weight_education, weight_crime, weight_income, weight_health, *toggle_clicks):
    visibility = [True, True, True, True, True]

    # Toggle visibility based on click counts
    for i, clicks in enumerate(toggle_clicks):
        if clicks and clicks % 2 == 1:
            visibility[i] = False

    weighted_data = modern_data.copy()
    weighted_data["IQ"] *= weight_iq
    weighted_data["Educational Attainment"] *= weight_education
    weighted_data["Crime Statistics"] *= weight_crime
    weighted_data["Income Disparity"] *= weight_income
    weighted_data["Health Outcomes"] *= weight_health

    fig = go.Figure()
    for col, color, is_visible in zip(
        ["IQ", "Educational Attainment", "Crime Statistics", "Income Disparity", "Health Outcomes"],
        ["#636EFA", "#EF553B", "#00CC96", "#AB63FA", "#FFA15A"],
        visibility
    ):
        if is_visible:
            fig.add_trace(go.Bar(x=weighted_data["Group"], y=weighted_data[col], name=col, marker=dict(color=color), opacity=0.75))

    fig.update_layout(
        barmode="group",
        plot_bgcolor="white",
        font=dict(family="Avenir"),
        xaxis=dict(showgrid=False, showline=True, zeroline=False, title="Group"),
        yaxis=dict(showgrid=True, showticklabels=False, title=""),
        showlegend=False,
        margin=dict(l=10, r=10, t=20, b=10)
    )
    return fig


if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
