import openpyxl
l1 = [
    [1,2,3,4,5],
    [2,4,6,8,10],
    [3,6,9,12,15],
    [4,8,12,16,20]
]
book = openpyxl.Workbook()
sheet = book.active
for i in range(1,5):
    for j in range(1,6):
        sheet.cell(row=i, column=j).value = l1[i-1][j-1]

book.save("listdata.xlsx")