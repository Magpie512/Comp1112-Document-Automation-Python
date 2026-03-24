"""
Mars Briggs
200561234
2026-03-24
Overdue Penalty Calculations
"""
import subprocess
import time
import ctypes
import openpyxl

# Collects col DEF with their columns going from 2 - 6
def collectTableInfo():
    wb=openpyxl.Workbook()
    sheet.wbactive
    sheet.title="Test"
    columnList = ["D","E","F"]
    for col in columnList:
        for row in range(4,6):   

def collectTimes():
    now = time.ctime()
    return now

#Calculate how many days have passed and convert into days
#def passedTime(now):
    

#def overDuePenalty(elapsedTime):

#def writeToFile:

#def userInterface:


print(collectTimes())
