import plotly.express as px
import pandas as pd

# Creating the biased dataset
biased_data = pd.DataFrame({
    "Group": ["White", "Black", "Asian", "Hispanic", "Other"],
    "IQ": [120, 85, 110, 95, 100],
    "Moral Character": [9.5, 6.0, 8.0, 7.0, 7.5],
    "Reproduction Rate": [1.8, 2.5, 1.6, 3.1, 2.0],
    "Crime Rate": [0.2, 0.8, 0.3, 0.5, 0.6],
    "Economic Output": [80_000, 35_000, 70_000, 50_000, 45_000]
})

# Creating the unbiased dataset (random values)
import numpy as np
unbiased_data = pd.DataFrame({
    "Group": ["White", "Black", "Asian", "Hispanic", "Other"],
    "IQ": np.random.randint(85, 115, 5),
    "Moral Character": np.random.uniform(6.0, 10.0, 5),
    "Reproduction Rate": np.random.uniform(1.5, 3.5, 5),
    "Crime Rate": np.random.uniform(0.2, 0.8, 5),
    "Economic Output": np.random.randint(30_000, 80_000, 5)
})

# Generate the biased visualization
biased_fig = px.bar(
    biased_data.melt(id_vars="Group", var_name="Variable", value_name="Score"),
    x="Group", y="Score", color="Variable",
    title="Biased Ethnic Group Data (Weighted Variables)",
    barmode="group"
)

# Generate the unbiased visualization
unbiased_fig = px.bar(
    unbiased_data.melt(id_vars="Group", var_name="Variable", value_name="Score"),
    x="Group", y="Score", color="Variable",
    title="Unbiased Ethnic Group Data (Randomized Variables)",
    barmode="group"
)

# Save the visualizations as HTML
biased_fig.write_html("/mnt/data/biased_ethnic_group_data.html")
unbiased_fig.write_html("/mnt/data/unbiased_ethnic_group_data.html")

("/mnt/data/biased_ethnic_group_data.html", "/mnt/data/unbiased_ethnic_group_data.html")
