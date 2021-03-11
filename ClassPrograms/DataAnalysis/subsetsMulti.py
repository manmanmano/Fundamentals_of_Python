import pandas as pd
data = pd.read_excel('Excel/sample.xlsx')
df = pd.DataFrame(data, columns=['Total', 'Unit Cost'])
print(df)
