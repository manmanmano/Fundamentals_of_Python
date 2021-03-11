import xlsxwriter
import random

workbook = xlsxwriter.Workbook('numAndPrice.xlsx')
worksheet = workbook.add_worksheet()

randomNums, randomPrices = [], []
for i in range(20):
    randomNums.append(random.randint(1, 100))
    randomPrices.append(random.uniform(1, 100))

worksheet.write('A1', 'Number')
worksheet.write('B1', 'Price')

row, column = 1, 0

for num in randomNums:
    worksheet.write(row, column, num)
    row += 1
row = 1
for price in randomPrices:
    worksheet.write(row, column + 1, "{:.2f}".format(price))
    row += 1

workbook.close()
