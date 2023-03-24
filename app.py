from openpyxl import Workbook

wb = load_workbook('subjetcs-data.xlsx')
ws = wb.active  # give the actual worksheet
wb.create_sheet('test')

print(ws)
print(ws['A2'].value)
print(wb.sheetnames)
print(wb['test'])

# ws['A2'].value = 'Carlos'

# wb.save('subjetcs-data.xlsx')

# print(ws['A2'].value)
