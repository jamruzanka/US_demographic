from openpyxl import Workbook

my_excel = Workbook()
ws1 = my_excel.active
ws2 = my_excel.create_sheet("Sheet_2")

my_file = open('demographic.txt', 'r')
column_letters = ["A", "B", "C", "D", "E", "F", "G"]
row_number = 0
column_number = 0
for line in my_file:
    elements = line[1:-1].split(",")
    print(">>>>> elements", elements)
    print(">>>>> line", line)
    if len(elements) > 1:
        for element in elements:
            ws1[column_letters[column_number]+str(row_number + 1)] = element
            column_number += 1
        row_number += 1
        column_number = 0
my_excel.save("my_excel_demographic.xlsx")
