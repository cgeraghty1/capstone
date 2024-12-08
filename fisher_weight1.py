import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Title
st.title("Fisher Visualization: Subjective Weightings")

# Generate random data
ethnic_data = pd.DataFrame({
    "Group": ["White", "Black", "Asian", "Hispanic", "Other"],
    "IQ": [100, 108, 105, 102, 98],
    "Moral Character": [95, 85, 90, 80, 85],
    "Violent Crime": [30, 35, 25, 40, 45],
    "Income": [75, 45, 70, 50, 55],
    "Reproduction Rate": [48, 55, 47, 60, 52]
})

# Sliders for weights
st.sidebar.title("Adjust Weights")
weights = {
    "IQ": st.sidebar.slider("IQ", 0.0, 5.0, 1.0, step=0.1),
    "Moral Character": st.sidebar.slider("Moral Character", 0.0, 5.0, 1.0, step=0.1),
    "Violent Crime": st.sidebar.slider("Violent Crime", 0.0, 5.0, 1.0, step=0.1),
    "Income": st.sidebar.slider("Income", 0.0, 5.0, 1.0, step=0.1),
    "Reproduction Rate": st.sidebar.slider("Reproduction Rate", 0.0, 5.0, 1.0, step=0.1),
}

# Apply weights to data
weighted_data = ethnic_data.copy()
for col, weight in weights.items():
    weighted_data[col] *= weight

# Plot the data
fig = go.Figure()
for col, color in zip(
    ["IQ", "Moral Character", "Violent Crime", "Income", "Reproduction Rate"],
    ["#636EFA", "#EF553B", "#00CC96", "#AB63FA", "#FFA15A"]
):
    fig.add_trace(go.Bar(x=weighted_data["Group"], y=weighted_data[col], name=col, marker=dict(color=color), opacity=0.75))

fig.update_layout(
    barmode="group",
    plot_bgcolor="white",
    font=dict(family="Avenir"),
    xaxis=dict(showgrid=False, showline=True, zeroline=False, title="Group"),
    yaxis=dict(showgrid=True, showticklabels=True, title="Value"),
    title="Weighted Variables by Group",
    margin=dict(l=10, r=10, t=40, b=10),
    height=500
)

# Display the chart
st.plotly_chart(fig)
