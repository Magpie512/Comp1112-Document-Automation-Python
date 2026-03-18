import openpyxl

ableToGraduate = []
noOutstandingfeesLibrary = []
noOutstandingfeesBookstore = []
noOutstandingfeesParking = []

applyToGraduate = openpyxl.load_workbook("C:\\openpyxl\\applyToGraduate.xlsx")
bookStoreOwed = openpyxl.load_workbook("C:\\openpyxl\\bookStoreOwed.xlsx")
libraryOwed = openpyxl.load_workbook("C:\\openpyxl\\libraryOwed.xlsx")
parkingOwed = openpyxl.load_workbook("C:\\openpyxl\\parkingOwed.xlsx")

wb = openpyxl.Workbook()
output = wb.active

# Bookstore
sheet = bookStoreOwed.active
for i in range (2,20):
    owed = sheet.cell(row=i,column=5).value
    if ( owed == 0): # acessing raw document
        noOutstandingfeesBookstore.append([str(sheet.cell(row=i,column=2).value),str(sheet.cell(row=i,column=3).value),str(sheet.cell(row=i,column=4).value),str(sheet.cell(row=i,column=5).value)])

# Library
sheet = libraryOwed.active
for i in range (2,20):
    owed = sheet.cell(row=i,column=5).value
    if ( owed == 0): # acessing raw document
        noOutstandingfeesLibrary.append([str(sheet.cell(row=i,column=2).value),str(sheet.cell(row=i,column=3).value),str(sheet.cell(row=i,column=4).value),str(sheet.cell(row=i,column=5).value)])

# Parking
sheet = parkingOwed.active
for i in range (2,20):
    owed = sheet.cell(row=i,column=5).value
    if ( owed == 0): # acessing raw document
        noOutstandingfeesParking.append([str(sheet.cell(row=i,column=2).value),str(sheet.cell(row=i,column=3).value),str(sheet.cell(row=i,column=4).value),str(sheet.cell(row=i,column=5).value)])

# Compare to see if student is eligible
for i in range(len(noOutstandingfeesBookstore)):
    if noOutstandingfeesBookstore[i][3] == "0" and noOutstandingfeesLibrary[i][3] == "0" and noOutstandingfeesParking[i][3] == "0":
        ableToGraduate.append([noOutstandingfeesBookstore[i][0],noOutstandingfeesBookstore[i][1],noOutstandingfeesBookstore[i][2],noOutstandingfeesBookstore[i][3]])

print(ableToGraduate)

for row in ableToGraduate:
    output.append(row)
newFile = "Eligible.xlsx"
wb.save(newFile)