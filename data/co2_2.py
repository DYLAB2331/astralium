import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read data from Excel file
file_path = './data/co2data.xlsx'
df = pd.read_excel(file_path)

# Calculate the percent change for each year
percent_change_per_year = df.groupby('year')['monthly average'].apply(lambda x: (x.iloc[-1] - x.iloc[0]) / x.iloc[0] * 100).reset_index()
percent_change_per_year.columns = ['year', 'Percent Change'] # Rename the columns

# Extract x and y values for the plot
x_percent_change = percent_change_per_year['year']
y_percent_change = percent_change_per_year['Percent Change']

# Perform linear regression on the percent change data
slope_percent_change, intercept_percent_change = np.polyfit(x_percent_change, y_percent_change, 1)
regression_y_percent_change = slope_percent_change * x_percent_change + intercept_percent_change

# Set up the plot with custom colors
plt.figure(figsize=[12, 6], facecolor='#1A1A1A')
plt.plot(x_percent_change, y_percent_change, marker='o', linestyle='-', color='orange', label='Percent Change')
plt.plot(x_percent_change, regression_y_percent_change, color='white', linestyle='--', linewidth=2, label='Regression Line')
plt.xlabel('Year', color='white')
plt.ylabel('Percent Change', color='white')
plt.title('Percent Change in Monthly Average per Year with Regression Line', color='white')
plt.tick_params(axis='both', colors='white')
plt.legend(loc='upper left')
plt.grid(True, linestyle='--', alpha=0.5)
plt.gca().set_facecolor('#1A1A1A')

# Show the plot
plt.show()
