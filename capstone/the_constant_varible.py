import matplotlib.pyplot as plt

# Define time periods and their associated variables
time_periods = ['1920s', '1950s', '1980s', '2000s', 'Present']
variables_by_period = [
    ["Race Purity", "Physical Health"],            # 1920s
    ["Socioeconomic Status", "Cultural Adaptability"],  # 1950s
    ["Educational Attainment", "Employment Levels"],    # 1980s
    ["Social Support", "Economic Productivity"],        # 2000s
    ["Well-being Index", "Social Mobility"]             # Present
]

# Plot setup
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot([0, len(time_periods)-1], [0, 0], color='black', linewidth=2, label="IQ (Constant)")

# Add time periods along the constant IQ line
for i, period in enumerate(time_periods):
    ax.text(i, 0.1, period, ha='center', va='bottom', fontsize=10, fontweight='bold')

    # Plot variables as nodes around the IQ line for each period
    for j, variable in enumerate(variables_by_period[i]):
        offset = (j + 1) * 0.15 if j % 2 == 0 else -(j + 1) * 0.15
        ax.plot(i, offset, 'o', color='blue' if i < 3 else 'green', markersize=8)
        ax.text(i, offset + 0.05, variable, ha='center', va='bottom', fontsize=8)

# Final adjustments to the plot
ax.set_ylim(-1, 1)
ax.axis('off')  # Hide axis lines for cleaner visualization
plt.title("Evolution of Variables in Statistical Analysis with IQ as a Constant Measure", fontsize=14)
plt.tight_layout()

# Show plot
plt.show()
