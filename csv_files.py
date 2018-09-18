import xlrd

file = xlrd.open_workbook('leave_code.xlsx')
sheet = file.sheet_by_index(0)

table = list()
record = list()

for x in range(sheet.nrows):
    for y in range(sheet.ncols):
        record.append(sheet.cell(x, y).value)
        table.append(record)
        # record = []

print(table)




