"""
Mars Briggs
03-17-26
200561234
Populating four spreadsheets with the same Fname and Lname, Student number
Seed each spreadsheet (2, 3, and 4) with a few unique names for testing

Write Eligible graduates to new spreadsheet
"""

# Imports
import openpyxl

applyToGraduate = openpyxl.load_workbook("C:\\openpyxl\\applyToGraduate.xlsx")
bookStoreOwed = openpyxl.load_workbook("C:\\openpyxl\\bookStoreOwed.xlsx")
libraryOwed = openpyxl.load_workbook("C:\\openpyxl\\libraryOwed.xlsx")
parkingOwed = openpyxl.load_workbook("C:\\openpyxl\\parkingOwed.xlsx")

# list declares
eligibleList = []
mainList = []
bookList =[]
libraryList = []
parkingList = []


wb = openpyxl.Workbook()
output = wb.active

# TEST for cycle
# for col in columnList:
#    for row in range(3, 20):
#        cellName = col + str(row)
#        value = application[cellName].value
#        print("Reading cell:", cellName, "Value:", value)

sheet = applyToGraduate.active
for r in range (2,20):
    idValue = sheet.cell(row=r,column=3).value
    if (idValue == None):
        break
    mainList.append([str(sheet.cell(row=r,column=2).value),str(sheet.cell(row=r,column=3).value),str(sheet.cell(row=r,column=4).value),str(sheet.cell(row=r,column=5).value)])

sheet = bookStoreOwed.active
for r in range (2,20):
    idValue = sheet.cell(row=r,column=3).value
    if (idValue == None):
        break
    bookList.append([str(sheet.cell(row=r,column=2).value),str(sheet.cell(row=r,column=3).value),str(sheet.cell(row=r,column=4).value),str(sheet.cell(row=r,column=5).value)])

sheet = libraryOwed.active
for r in range (2,20):
    idValue = sheet.cell(row=r,column=3).value
    if (idValue == None):
        break
    libraryList.append([str(sheet.cell(row=r,column=2).value),str(sheet.cell(row=r,column=3).value),str(sheet.cell(row=r,column=4).value),str(sheet.cell(row=r,column=5).value)])

parking = parkingOwed.active
for r in range (2,20):
    idValue = sheet.cell(row=r,column=3).value
    if (idValue == None):
        break
    parkingList.append([str(sheet.cell(row=r,column=2).value),str(sheet.cell(row=r,column=3).value),str(sheet.cell(row=r,column=4).value),str(sheet.cell(row=r,column=5).value)])

# Comparison

# Build fast lookup sets of IDs who owe money
bookIDs = {row[1] for row in bookList}
libraryIDs = {row[1] for row in libraryList}
parkingIDs = {row[1] for row in parkingList}

for row in mainList:
    studentID = row[1]

    if (studentID not in bookIDs 
        and studentID not in libraryIDs 
        and studentID not in parkingIDs):
        eligibleList.append(row)
print(eligibleList)

for row in eligibleList:
    output.append(row)
newFile = "Eligible.xlsx"
wb.save(newFile)

#print(bookList)
#print(libraryList)
#print(parkingList)
