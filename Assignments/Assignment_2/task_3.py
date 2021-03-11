import pandas as pd

table1 = pd.read_excel(r'Excel/proplayers1.xlsx')
table2 = pd.read_excel(r'Excel/proplayers2.xlsx')

frames = [table1, table2]

result = pd.concat(frames)

print(result)
