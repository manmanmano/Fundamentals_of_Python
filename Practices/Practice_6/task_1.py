import pandas as pd

data = pd.read_excel('Excel/numAndPrice.xlsx')
data['Result'] = data['Number'] * data['Price']

print(data.Result)
