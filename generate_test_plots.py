import numpy as np
import plotly.graph_objects as go
import webbrowser

# Seed for reproducibility
np.random.seed(42)

# Define the groups and variables
ethnic_groups = ['Ethnic Group A', 'Ethnic Group B', 'Ethnic Group C', 'Ethnic Group D', 'Ethnic Group E']

# Historical variables for biased dataset
historical_variables = ['IQ scores', 'Violent crime per 100 people', 'Economic output', 'Moral character score', 'Reproduction rates']

# Contemporary variables for unbiased dataset
contemporary_variables = ['IQ scores', 'GDP per capita', 'Degree-level education', 'Crime rate per 100 people', 'Physical health']

# Biased dataset (favoring Ethnic Group A and Ethnic Group C for IQ scores and moral character score)
biased_data = {
    'Ethnic Group A': [120, 15, 90000, 95, 3.5],
    'Ethnic Group B': [85, 15, 85000, 60, 2.8],
    'Ethnic Group C': [110, 18, 92000, 90, 4.0],
    'Ethnic Group D': [95, 14, 80000, 70, 3.2],
    'Ethnic Group E': [100, 16, 88000, 85, 3.0]
}

# Apply logarithmic scaling to the economic output (index 2 in the list)
for group in biased_data:
    biased_data[group][2] = np.log10(biased_data[group][2])

# Adjust IQ and Moral Character Scores for A and C, ensuring they have a slight bias but not extreme
for group in biased_data:
    if group in ['Ethnic Group A', 'Ethnic Group C']:  
        biased_data[group][0] = (biased_data[group][0] / 120) * 30  # Biased IQ for A and C (slightly higher)
        biased_data[group][3] = (biased_data[group][3] / 95) * 28  # Biased Moral Character for A and C
    else:
        biased_data[group][0] = (biased_data[group][0] / 120) * 26  # Balanced IQ for others
        biased_data[group][3] = (biased_data[group][3] / 95) * 24  # Balanced Moral Character for others

# Randomize Violent Crime, Economic Output, and Reproduction Rates for all groups with no correlation
for group in biased_data:
    biased_data[group][1] = np.random.uniform(10, 20)  # Randomize Violent Crime per 100 people
    biased_data[group][2] = np.random.uniform(12, 20)  # Randomize Economic Output
    biased_data[group][4] = np.random.uniform(10, 15)  # Randomize Reproduction rates

# Unbiased dataset using modern variables
unbiased_data = {
    'Ethnic Group A': np.random.randint(10, 30, len(contemporary_variables)),
    'Ethnic Group B': np.random.randint(10, 30, len(contemporary_variables)),
    'Ethnic Group C': np.random.randint(10, 30, len(contemporary_variables)),
    'Ethnic Group D': np.random.randint(10, 30, len(contemporary_variables)),
    'Ethnic Group E': np.random.randint(10, 30, len(contemporary_variables))
}

# Function to plot grouped bar chart with reduced opacity and auto-open in browser
def plot_grouped_bars(data, title, file_name, variables):
    fig = go.Figure()

    # Create a bar for each variable
    for i, var in enumerate(variables):
        fig.add_trace(go.Bar(
            x=ethnic_groups,
            y=[data[group][i] for group in ethnic_groups],
            name=var,
            opacity=0.75,  # Reduce opacity by 25%
        ))

    # Update layout
    fig.update_layout(
        title=title,
        xaxis_title="Ethnic Groups",
        yaxis_title="Normalized Scores",
        barmode='group',  # Use 'group' for grouped bars
        legend_title="Variables",
        plot_bgcolor='rgba(0,0,0,0)',  # Transparent background
        font=dict(size=14),
        bargap=0.2  # Space between bars
    )

    # Save the plot as an HTML file for embedding
    fig.write_html(file_name)

    # Automatically open the saved HTML file in the default browser
    webbrowser.open(f'file://{file_name}')

# Plot the biased and unbiased datasets, and save as HTML files with different variable sets
plot_grouped_bars(biased_data, "Biased Dataset", 'f_biased_data_plot.html', historical_variables)
plot_grouped_bars(unbiased_data, "Unbiased Dataset", 'f_unbiased_data_plot.html', contemporary_variables)
