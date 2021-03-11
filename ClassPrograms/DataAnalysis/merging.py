import pandas as pd
data = pd.read_excel('Excel/olympicsports.xlsx')
data1 = pd.read_excel('Excel/olympicsport.xlsx')
merged = pd.merge(data, data1)
print(merged)
