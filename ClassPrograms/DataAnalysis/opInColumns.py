import pandas as pd
data = pd.read_excel('Excel/sample.xlsx')
data['New_Col'] = data['Units'] + data['Unit Cost']
print(data.New_Col)
