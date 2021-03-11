import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

dataframe = pd.read_excel('Excel/numAndPrice.xlsx')
x = dataframe.Number
y = dataframe.Price
stats = linregress(x, y)
m = stats.slope
b = stats.intercept

plt.figure(figsize = (10, 10))
plt.scatter(x, y, marker = '*')
plt.plot(x, m * x + b, color="orange", linewidth=3)

plt.xlabel("Numbers", fontsize = 20)
plt.ylabel("Prices", fontsize = 20)
plt.xticks(fontsize = 18)
plt.yticks(fontsize = 18)
plt.show()
