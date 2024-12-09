import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the biased dataset CSV from your specified file path
file_path = '/Users/colingeraghty/Documents/Fisher test Data Vis/biased_dataset.csv'
biased_df = pd.read_csv(file_path)

# Prepare the data for visualization
visualization_data = biased_df.groupby('Country').mean().reset_index()
visualization_data = visualization_data.sort_values(by='Moral character score', ascending=False)

# Normalize the scores to get values between 0 and 1 for color mapping
norm = plt.Normalize(visualization_data['Moral character score'].min(), visualization_data['Moral character score'].max())
sm = plt.cm.ScalarMappable(cmap="Reds", norm=norm)
sm.set_array([])  # This line may be necessary to avoid warnings in some matplotlib versions

# Create the bar plot for 'Moral character score' with the specified aesthetic changes
plt.figure(figsize=(12, 6))
ax = sns.barplot(x='Country', y='Moral character score', data=visualization_data, palette=sm.to_rgba(visualization_data['Moral character score']))

# Set plot labels and title
ax.set_title('Mean Moral Character Score by Country Showing Bias')
ax.set_xlabel('')
ax.set_ylabel('')

# Remove all the labels for a clean look
ax.set_xticklabels([])
ax.set_yticklabels([])

# Set the edge color of the bars
for bar in ax.patches:
    bar.set_edgecolor('gray')
    bar.set_linewidth(1)
    bar.set_alpha(0.5)  # Set the fill alpha to 50%

# Change the axes to gray
ax.spines['bottom'].set_color('gray')
ax.spines['left'].set_color('gray')

# Save the figure to a PDF file with white background and gray fonts/lines
plt.savefig('/Users/colingeraghty/Documents/Fisher test Data Vis/moral_character_score_plot.pdf', 
            bbox_inches='tight', 
            transparent=True, 
            facecolor='white')

# Show the plot
plt.show()
