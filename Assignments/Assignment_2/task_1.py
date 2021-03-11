import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel(r'Excel/seconds.xlsx')
plt.hist(df, bins=5, color="green", density=True)

plt.title('Customer wait time')
plt.xlabel('Seconds')
plt.ylabel('Occurences')

plt.show()
