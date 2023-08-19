import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

file_path = "./data/co2data.xlsx"

# Read data from Excel and store in data as rows
df = pd.read_excel(file_path)

# Set x and y 
x = df['year'] + (df['month'] - 1) / 12
y = df['monthly average']

# Plot monthy average line graph
plt.figure(figsize = [12, 6], facecolor = '#1A1A1A')
plt.gca().set_facecolor('#1A1A1A')
plt.plot(x, y, color = 'orange', linewidth = 2)
plt.xlabel('Year', color = 'white')
plt.ylabel('Monthly Average', color = 'white')
plt.title('Monthly Average Over Time', color = 'white')
plt.tick_params(axis = 'both', colors = 'white')
plt.ylim(min(y) - 5, max(y) + 5)
plt.grid(True, linestyle = '--', alpha = 0.5)
plt.show()
