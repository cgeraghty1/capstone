import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Title
st.title("Fisher Statistical Visualization")

# Generate random data
fisher_data = pd.DataFrame({
    "Group": ["White", "Black", "Asian", "Hispanic", "Other"],
    "IQ": [100, 108, 105, 102, 98],
    "Moral Character": [95, 85, 90, 80, 85],
    "Violent Crime": [30, 35, 25, 40, 45],
    "Income": [75, 45, 70, 50, 55],
    "Reproduction Rate": [48, 55, 47, 60, 52]
})

# Sidebar for variable selection
st.sidebar.title("Adjust Variables")

# Checkboxes to toggle visibility of variables
visible_columns = {}
for col in ["IQ", "Moral Character", "Violent Crime", "Income", "Reproduction Rate"]:
    visible_columns[col] = st.sidebar.checkbox(col, value=True)

# Sliders to adjust weights
weights = {
    col: st.sidebar.slider(f"{col} Weight", 0.0, 5.0, 1.0, step=0.1)
    for col in visible_columns if visible_columns[col]
}

# Apply weights to data
weighted_data = fisher_data.copy()
for col, weight in weights.items():
    weighted_data[col] *= weight

# Plot the data
fig = go.Figure()

for col, color in zip(
    ["IQ", "Moral Character", "Violent Crime", "Income", "Reproduction Rate"],
    ["#636EFA", "#EF553B", "#00CC96", "#AB63FA", "#FFA15A"]
):
    if visible_columns[col]:
        fig.add_trace(go.Bar(
            x=weighted_data["Group"],
            y=weighted_data[col],
            name=col,
            marker=dict(color=color),
            opacity=0.75
        ))

fig.update_layout(
    barmode="group",
    plot_bgcolor="white",
    font=dict(family="Avenir"),
    xaxis=dict(showgrid=False, showline=True, zeroline=False, title="Group"),
    yaxis=dict(showgrid=True, title="Weighted Value"),
    margin=dict(l=10, r=10, t=40, b=10),
    height=500
)

# Display chart
st.plotly_chart(fig)
