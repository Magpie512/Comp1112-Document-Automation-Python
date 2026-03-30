"""
Mars Briggs
200561234
2026-03-30 1:15 PM
Game Price Point comparison
"""

import urllib.request
from bs4 import BeautifulSoup
import openpyxl
import os
import datetime
import time

"""
Logic Guide:
disclose                # Display user warning and use guide
siteInput               # Collects sites into siteList
gameInput               # Collects game titles into gameList
vvv
createWorkbook          # initialize excel sheet
excelHeader             # create the column headers
vvv
fetchPage               # retrieve the target url
findGame                # find the target game
isPriceSymbol           # Identify price tag 
findPrice               # Find the price
scrapePrice             # Get the price
vvv
writeToExcel            # populates the rows
saveExcel               # saves the file
notifyUser              # notifies the user of finished execution
openProgram             # opens the saved file via default program (mycase is LibreOffice Calc)
waitUntilMidnight       # Delay execution until the next day
deleteExistingFile      # removes old file.
"""

# Globals
priceBook = None
priceSheet = None
websiteList = []
gameTitleList = []

# User Input

# User guide and warning
def disclose():
    print("This program compares game prices between websites.")
    print("Provide sites that show game titles AND prices.")
    print("Sites requiring login will not work.\n")

# Asks user for sites to use inside of a while loop to ensure multiple sites if needed
def siteInput():
    addingMore = True
    while addingMore:
        site = input("Enter a website: ").strip()
        websiteList.append(site)
        print("Added " + site + " to the list.")
        print("Would you like to add another? (Y/N)")
        if input().strip().upper() == "N":
            addingMore = False

# Asks user for games to use inside of the same logic as above
def gameInput():
    addingMore = True
    while addingMore:
        game = input("Enter a game title: ").strip()
        gameTitleList.append(game)
        print("Added " + game + " to the list.")
        print("Would you like to add another? (Y/N)")
        if input().strip().upper() == "N":
            addingMore = False

# Excel Management Functions 

# Initializes the Excel workbook
def createWorkbook():
    global priceBook, priceSheet
    priceBook = openpyxl.Workbook()
    priceSheet = priceBook.active

# Creates the column headers
def excelHeader():
    priceSheet["A1"] = "Game(s)"
    priceSheet["B1"] = "Site(s)"
    priceSheet["C1"] = "Price(s)"

# Populates the rows of the newly created Excel sheet
def writeToExcel(resultsList):
    rowIndex = 2
    for game, site, price in resultsList:
        priceSheet.cell(row=rowIndex, column=1).value = game
        priceSheet.cell(row=rowIndex, column=2).value = site
        priceSheet.cell(row=rowIndex, column=3).value = price
        rowIndex += 1 # christ did we learn this in class? can I assume this?

# Save le file to excel
def saveExcel():
    try:
        priceBook.save("gamePrices.xlsx")
    except PermissionError as e:
        print("Error: " + str(e))

# deletes the existing file file its there
def deleteExistingFile():
    if os.path.exists("gamePrices.xlsx"):
        try:
            os.remove("gamePrices.xlsx")
        except PermissionError as e:
            print("Error: " + str(e))

# --- Scraping Logic Functions ---

def fetchPage(targetSite):
    try:
        html = urllib.request.urlopen(targetSite).read()
        soup = BeautifulSoup(html, "html.parser")
        return soup.get_text()
    except Exception as e:
        print("Error reaching " + targetSite + ": " + str(e))
        return None

def findGame(pageText, targetGame):
    return targetGame.lower() in pageText.lower()

def isPriceSymbol(word):
    # Simpler logic: check if the first character is a dollar sign
    if len(word) > 1:
        if word[0] == "$":
            return True
    return False

def findPrice(pageText):
    words = pageText.split()
    for word in words:
        if isPriceSymbol(word):
            # Just return the word found; no complex filtering
            return word
    return "No price found"

def scrapePrice(targetSite, targetGame):
    pageText = fetchPage(targetSite)
    if pageText is None:
        return "Error reaching site"
    if not findGame(pageText, targetGame):
        return "Game not found"
    return findPrice(pageText)

# --- Utility Functions ---

def notifyUser():
    print("Results saved to gamePrices.xlsx")

def openProgram():
    try:
        os.startfile("gamePrices.xlsx")
    except Exception:
        print("Could not open file automatically.")

def waitUntilMidnight():
    now = datetime.datetime.now()
    tomorrow = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(days=1)
    # Calculate exact sleep duration
    seconds_to_wait = (tomorrow - now).total_seconds()
    time.sleep(seconds_to_wait)

# --- Main Program Execution ---

disclose()
input("Press Enter to begin setup...")
siteInput()
gameInput()

# Initial Setup
createWorkbook()
excelHeader()

endDate = datetime.datetime.now() + datetime.timedelta(days=7)

while datetime.datetime.now() < endDate:
    cycleResults = []

    for gameTitle in gameTitleList:
        for website in websiteList:
            foundPrice = scrapePrice(website, gameTitle)
            cycleResults.append([gameTitle, website, foundPrice])

    writeToExcel(cycleResults)
    saveExcel()
    notifyUser()
    openProgram()
    
    # Wait until the next day, then clear and re-initialize
    waitUntilMidnight()
    deleteExistingFile()
    createWorkbook()
    excelHeader()