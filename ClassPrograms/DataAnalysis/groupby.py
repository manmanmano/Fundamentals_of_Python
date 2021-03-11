import pandas as pd
data = pd.read_excel('Excel/sample.xlsx')
group = data.groupby('Unit Cost')
print(group.get_group(1.99))
