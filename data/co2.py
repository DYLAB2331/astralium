import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

file_path = "./data/co2data.xlsx"
df = pd.read_excel(file_path)

plt.plot(df['decimal date'], df['monthly average'])
plt.xlabel('Decimal Date')
plt.ylabel('Monthly Average')
plt.title('Monthly Average over Time')
plt.show()


