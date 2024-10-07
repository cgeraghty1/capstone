import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Define the data
data = {
    'IQ Scores': [88, 70, 60, 52],
    'Physical Health and Vitality': [78, 88, 73, 71],
    'Reproductive Success': [64, 68, 85, 51],
    'Moral Character and Criminality': [92, 72, 89, 73],
    'Economic Productivity': [57, 60, 73, 93]
}
groups = ['Group A', 'Group B', 'Group C', 'Group D']
colors = ['red', 'blue', 'green', 'orange']  # Define colors for each group

# Calculate the mean and standard deviation of the IQ scores
iq_scores = data['IQ Scores']
mean_iq = np.mean(iq_scores)
std_iq = np.std(iq_scores)

# Generate points on the x axis between -3 and 3 standard deviations of the mean
points = np.linspace(mean_iq - 3*std_iq, mean_iq + 3*std_iq, 100)

# Plot the bell curve
plt.plot(points, norm.pdf(points, mean_iq, std_iq), linestyle='dotted')

# Plot each group's IQ score on the bell curve
for group, color in zip(iq_scores, colors):
    plt.plot(group, norm.pdf(group, mean_iq, std_iq), 'o', color=color)

# Add a legend
plt.legend(['Mean IQ (Dotted Bell Curve)'] + groups)

# Show the plot
plt.title('Bell Curve Comparison of IQ Scores')
plt.xlabel('IQ Scores')
plt.ylabel('Probability Density')

# Display the plot
plt.show()
