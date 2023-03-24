from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Data"

ws.append(['TIm', 'is', 'great', '!'])
ws.append(['TIm', 'is', 'great', '!'])
ws.append(['TIm', 'is', 'great', '!'])
ws.append(['TIm', 'is', 'great', '!'])
ws.append(['end'])

wb.save('tim.xlsx')
