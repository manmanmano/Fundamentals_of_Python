import pandas as pd
data = pd.read_excel('Excel/olympicsports.xlsx')
df = pd.DataFrame(data, columns=['SportID'])
print(df)
