import openpyxl

book = openpyxl.load_workbook("C:/Users/Stephin Philip A/Downloads/download.xlsx")
sheet = book.active
Dict = {}
cell = sheet.cell(row=1, column=2)
print(cell.value)
sheet.cell(row=1, column=2).value = "Stephin"

print(sheet.cell(row=1, column=2).value)

print(sheet.max_row)

print(sheet.max_column)

print(sheet.min_column)