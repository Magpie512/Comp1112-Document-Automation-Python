"""
Mars Briggs
200561234
2026-03-24
Overdue Penalty Calculations
"""

import time
import openpyxl
from datetime import datetime
import subprocess

invoicesSheet = openpyxl.load_workbook(r"C:\Lesson 10\Test.xlsx")
sheet = invoicesSheet.active

# Reads and Collects the info from the columns
def collectTableInfo():
    columnList = ["D", "E", "F"]
    collectedInfo = []
    # Column itratove
    for col in columnList:
        tempList = []
        for row in range(2, 7):
            cellValue = sheet[col + str(row)].value
            tempList.append(cellValue)
        collectedInfo.append(tempList)
    return collectedInfo

# Returns The Current time 
def collectTimes():
    return time.ctime()

# Passed time from the now
def passedTime(dueDate):
    today = datetime.now()
    elapsedTime = today - dueDate
    return elapsedTime.days

# Calculates the overdue penalty from the percentage column (6)
def overDuePenalty(daysLate, rate=2.00):
    if daysLate <= 0:
        return 0
    return daysLate * rate

# write to file
def writeToFile(data):
    #moved from top to keep concise
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Outstanding Invoices"
    ws.append(["Invoice #", "Amount", "Due Date", "Days Late", "Penalty"])
    for row in data:
        ws.append(row)
    wb.save("OutstandingInvoices.xlsx")
    
# Open calc and open file
def userInterface():
    subprocess.Popen([r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\LibreOffice\LibreOffice Calc.lnk","C:\Lesson 10\Test.xlsx"])

# TEST CODE


"""
def main():
    table = collectTableInfo()
    invoiceNums = table[0]
    amounts = table[6]
    dueDates = table[5]
    results = []

    for i in range(len(invoiceNums)):
        inv = invoiceNums[i]
        amt = amounts[i]
        due = dueDates[i]

        daysLate = passedTime(due)
        penalty = overDuePenalty(daysLate)

        results.append([inv, amt, due, daysLate, penalty])

    writeToFile(results)
    userInterface()

main()
"""