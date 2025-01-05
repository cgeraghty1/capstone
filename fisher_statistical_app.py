import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd

# Initialize the Dash app
app = dash.Dash(__name__)
app.title = "Industry Impact Visualization"

# Sample data
data = pd.DataFrame({
    "Industry": ["Big Pharma", "Oil Industry", "Tech Industry", "Industrial Agriculture", "Luxury Goods"],
    "Environmental Harm": [90, 70, 60, 85, 75],
    "Resource Exploitation": [85, 79, 75, 80, 71],
    "Worker Mistreatment": [70, 80, 65, 90, 60],
    "Deceptive Practices": [80, 85, 90, 75, 70],
    "Lobbying Influence": [85, 76, 80, 70, 60]
})

# App layout
app.layout = html.Div([
    # Top row with bar chart and sliders
    html.Div([
        # Bar Chart Section
        html.Div([
            dcc.Graph(id="bar-chart", style={"width": "100%", "height": "400px"})
        ], style={"width": "60%", "padding-right": "10px"}),

        # Sliders Section
        html.Div([
            html.Div([
                html.Div([
                    html.Label("Environmental Harm", style={"font-family": "Avenir", "font-size": "12px", "color": "#636EFA", "font-weight": "bold"}),
                    dcc.Slider(
                        id="weight-environment",
                        min=0, max=5, step=0.1, value=1,
                        marks={i: str(i) for i in range(6)},
                        tooltip={"placement": "bottom", "always_visible": False}
                    )
                ], style={"margin-bottom": "5px"}),
                html.Div([
                    html.Label("Resource Exploitation", style={"font-family": "Avenir", "font-size": "12px", "color": "#EF553B", "font-weight": "bold"}),
                    dcc.Slider(
                        id="weight-resource",
                        min=0, max=5, step=0.1, value=1,
                        marks={i: str(i) for i in range(6)},
                        tooltip={"placement": "bottom", "always_visible": False}
                    )
                ], style={"margin-bottom": "5px"}),
                html.Div([
                    html.Label("Worker Mistreatment", style={"font-family": "Avenir", "font-size": "12px", "color": "#00CC96", "font-weight": "bold"}),
                    dcc.Slider(
                        id="weight-worker",
                        min=0, max=5, step=0.1, value=1,
                        marks={i: str(i) for i in range(6)},
                        tooltip={"placement": "bottom", "always_visible": False}
                    )
                ], style={"margin-bottom": "5px"}),
                html.Div([
                    html.Label("Deceptive Practices", style={"font-family": "Avenir", "font-size": "12px", "color": "#AB63FA", "font-weight": "bold"}),
                    dcc.Slider(
                        id="weight-deceptive",
                        min=0, max=5, step=0.1, value=1,
                        marks={i: str(i) for i in range(6)},
                        tooltip={"placement": "bottom", "always_visible": False}
                    )
                ], style={"margin-bottom": "5px"}),
                html.Div([
                    html.Label("Lobbying Influence", style={"font-family": "Avenir", "font-size": "12px", "color": "#FFA15A", "font-weight": "bold"}),
                    dcc.Slider(
                        id="weight-lobbying",
                        min=0, max=5, step=0.1, value=1,
                        marks={i: str(i) for i in range(6)},
                        tooltip={"placement": "bottom", "always_visible": False}
                    )
                ], style={"margin-bottom": "5px"})
            ], style={"display": "flex", "flex-direction": "column", "justify-content": "space-around"})
        ], style={"width": "40%", "padding-left": "10px", "padding-top": "30px"})
    ], style={"display": "flex", "justify-content": "space-between", "align-items": "flex-start"}),

    # Bottom row with total scores
    html.Div([
        dcc.Graph(id="total-scores", style={"width": "100%", "height": "300px"})
    ], style={"margin-top": "0px"})
])

# Callbacks
@app.callback(
    [Output("bar-chart", "figure"), Output("total-scores", "figure")],
    [Input("weight-environment", "value"),
     Input("weight-resource", "value"),
     Input("weight-worker", "value"),
     Input("weight-deceptive", "value"),
     Input("weight-lobbying", "value")]
)
def update_charts(weight_environment, weight_resource, weight_worker, weight_deceptive, weight_lobbying):
    # Apply weights
    weighted_data = data.copy()
    weighted_data["Environmental Harm"] *= weight_environment
    weighted_data["Resource Exploitation"] *= weight_resource
    weighted_data["Worker Mistreatment"] *= weight_worker
    weighted_data["Deceptive Practices"] *= weight_deceptive
    weighted_data["Lobbying Influence"] *= weight_lobbying

    # Total scores
    weighted_data["Total Score"] = (
        weighted_data["Environmental Harm"] +
        weighted_data["Resource Exploitation"] +
        weighted_data["Worker Mistreatment"] +
        weighted_data["Deceptive Practices"] +
        weighted_data["Lobbying Influence"]
    )

    # Normalize total scores for gradient effect
    max_score = weighted_data["Total Score"].max()
    min_score = weighted_data["Total Score"].min()

    # Handle edge case: all scores equal
    if max_score == min_score:
        normalized_scores = [0.5] * len(weighted_data["Total Score"])
    else:
        normalized_scores = (weighted_data["Total Score"] - min_score) / (max_score - min_score)

    # Ensure minimum visibility for lower scores
    colors = ["rgba(255, 0, 0, {:.2f})".format(0.2 + score * 0.8) for score in normalized_scores]

    # Bar Chart
    bar_chart = go.Figure()
    for col, color in zip(
        ["Environmental Harm", "Resource Exploitation", "Worker Mistreatment", "Deceptive Practices", "Lobbying Influence"],
        ["#636EFA", "#EF553B", "#00CC96", "#AB63FA", "#FFA15A"]
    ):
        bar_chart.add_trace(go.Bar(
            x=weighted_data["Industry"],
            y=weighted_data[col],
            name=col,
            marker=dict(color=color, opacity=0.8)
        ))
    bar_chart.update_layout(
        barmode="group",
        template="simple_white",
        showlegend=False,
        xaxis=dict(
            showline=False,        # Remove x-axis line
            zeroline=False,        # Remove x-axis zero line
            showticklabels=True,   # Keep x-axis tick labels
            showgrid=False,        # Remove x-axis gridlines
        ),
        yaxis=dict(
            showline=False,        # Remove y-axis line
            zeroline=False,        # Remove y-axis zero line
            showticklabels=True,   # Keep y-axis tick labels
            showgrid=False         # Remove y-axis gridlines
        )
    )

    # Total Scores Bar
    total_scores = go.Figure()
    total_scores.add_trace(go.Bar(
        y=weighted_data["Industry"],
        x=weighted_data["Total Score"],
        orientation="h",
        marker=dict(color=colors),
        width=0.5  # Skinnier bars
    ))
    total_scores.update_layout(
        template="simple_white",
        xaxis=dict(
            showline=False,        # Remove x-axis line
            zeroline=False,        # Remove x-axis zero line
            showticklabels=False,  # Remove x-axis tick labels
            showgrid=False,        # Remove x-axis gridlines
        ),
        yaxis=dict(
            showline=False,        # Remove y-axis line
            zeroline=False,        # Remove y-axis zero line
            showticklabels=True,   # Keep y-axis tick labels for industries
            showgrid=False,        # Remove y-axis gridlines
            tickmode="array",
            tickvals=list(range(len(data))),
            ticktext=data["Industry"],
            automargin=True,
            tickfont=dict(size=12)
        ),
        margin=dict(l=120, r=20, t=10, b=10),
        bargap=0.1  # Reduced gap between bars
    )

    return bar_chart, total_scores

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run_server(debug=True, host="0.0.0.0", port=port)




