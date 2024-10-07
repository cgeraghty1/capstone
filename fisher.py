import numpy as np
import plotly.graph_objects as go
import webbrowser

# Seed for reproducibility
np.random.seed(42)

# Define the countries and variables
countries = ['Country A', 'Country B', 'Country C', 'Country D', 'Country E']
variables = ['IQ scores', 'Violent crime per 100 people', 'Economic output', 'Moral character score', 'Reproduction rates']

# Create biased dataset (favoring Country A and Country C for IQ scores)
biased_data = {
    'Country A': [120, 10, 90000, 95, 3.5],
    'Country B': [85, 20, 85000, 60, 2.8],
    'Country C': [110, 8, 92000, 90, 4.0],
    'Country D': [95, 18, 80000, 70, 3.2],
    'Country E': [100, 15, 88000, 85, 3.0]
}

# Apply logarithmic scaling to the economic output (index 2 in the list)
for country in biased_data:
    biased_data[country][2] = np.log10(biased_data[country][2])

# Normalize the biased data to avoid large differences and apply IQ bias
for country in biased_data:
    if country in ['Country A', 'Country C']:  # Bias towards these countries
        biased_data[country] = [x / max(biased_data[country]) * 120 for x in biased_data[country]]
    else:
        biased_data[country] = [x / max(biased_data[country]) * 100 for x in biased_data[country]]

# Unbiased dataset (random scores between 50 and 100)
unbiased_data = {
    'Country A': np.random.randint(50, 100, len(variables)),
    'Country B': np.random.randint(50, 100, len(variables)),
    'Country C': np.random.randint(50, 100, len(variables)),
    'Country D': np.random.randint(50, 100, len(variables)),
    'Country E': np.random.randint(50, 100, len(variables))
}

# Function to plot grouped bar chart with reduced opacity and auto-open in browser
def plot_grouped_bars(data, title, file_name):
    fig = go.Figure()

    # Create a bar for each variable
    for i, var in enumerate(variables):
        fig.add_trace(go.Bar(
            x=countries,
            y=[data[country][i] for country in countries],
            name=var,
            opacity=0.75,  # Reduce opacity by 25%
        ))

    # Update layout
    fig.update_layout(
        title=title,
        xaxis_title="Countries",
        yaxis_title="Normalized Scores",
        barmode='group',  # Use 'stack' for stacked bars
        legend_title="Variables",
        plot_bgcolor='rgba(0,0,0,0)',  # Transparent background
        font=dict(size=14),
        bargap=0.2  # Space between bars
    )

    # Save the plot as an HTML file for embedding
    fig.write_html(file_name)

    # Automatically open the saved HTML file in the default browser
    webbrowser.open(f'file://{file_name}')

# Plot the biased and unbiased datasets, and save as HTML files
plot_grouped_bars(biased_data, "Biased Dataset - Emphasizing 'IQ scores' and 'Moral character score'", 'biased_data_plot.html')
plot_grouped_bars(unbiased_data, "Unbiased Dataset - Random Scores", 'unbiased_data_plot.html')
