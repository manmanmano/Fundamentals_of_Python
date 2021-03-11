import pandas as pd

data = pd.read_excel('Excel/numAndPrice.xlsx')
group = data.groupby('Number')

print(group.get_group(99))
