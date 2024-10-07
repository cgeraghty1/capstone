# Adjusting the script to change group colors and remove the outermost circle

# Importing necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi

# Data for the DataFrame
data = {
    'IQ Scores': [88, 70, 60, 52],
    'Physical Health and Vitality': [78, 88, 73, 71],
    'Reproductive Success': [64, 68, 85, 51],
    'Moral Character Score': [92, 72, 89, 73],
    'Economic Productivity': [57, 60, 73, 93]
}
groups = ['Group A', 'Group B', 'Group C', 'Group D']
df = pd.DataFrame(data, index=groups)

# Define the number of variables
num_vars = len(df.columns)

# Compute angle for each axis
angles = [n / float(num_vars) * 2 * pi for n in range(num_vars)]
angles += angles[:1]  # Complete the loop

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Draw one axe per variable and add labels
plt.xticks(angles[:-1], df.columns, color='grey', size=10)

# Draw ylabels
plt.yticks([25, 50, 75, 100], ["25", "50", "75", "100"], color="grey", size=7)
plt.ylim(0, 100)

# Define colors for each group
colors = ['red', 'blue', 'green', 'orange']

# Plot data with the specified colors for each group
for idx, row in df.iterrows():
    values = row.tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='solid', label=idx, color=colors[groups.index(idx)])

# Add legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

# Remove the outermost circle line by setting the visibility of the outline to False
ax.spines['polar'].set_visible(False)

# Manually adjust the label position of "IQ Scores" if needed
label = ax.get_xticklabels()[0]
label.set_verticalalignment('bottom')

# Display the plot without filling
plt.savefig('radar_chart.pdf', bbox_inches='tight')
plt.show()





