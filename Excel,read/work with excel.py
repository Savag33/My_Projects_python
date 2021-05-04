
import openpyxl

book = openpyxl.open("Учні.xlsx", read_only=True)

sheet = book.active

print(sheet["B2"].value)
print(sheet[5][1].value)
print()

for row in range(1,sheet.max_row):
    surname = sheet[row][0].value
    name = sheet[row][1].value
    year = sheet[row][2].value
    height = sheet[row][3].value
    print(row, surname,name,year,height)

book.close()




