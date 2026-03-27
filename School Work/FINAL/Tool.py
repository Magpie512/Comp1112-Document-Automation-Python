"""
Mars Briggs
200561234
2026-03-20
Game Price Point comparisson (that aint spelled right)
"""
# need to map out the logic on a whiteboard to see if i can improve any logic
# also need to try except. thank you michael for 

# For Web scraping
import urllib.request
from bs4 import BeautifulSoup
import openpyxl # For Excel
import os # Mike says its okay
import datetime
import time

# Function to wait for site refresh(or rather estimated refresh(real refresh could be 3am pst for all I know))
def refresh():
    now = datetime.datetime.now()
    # Sets midnight by taking today's date and adding exactly one day (I imagine this will make jillian make fun of me but i probably most definitely deserve it)
    midnight = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(days=1)
    while datetime.datetime.now() < midnight:
        time.sleep(3600) # 3600 seconds = 1 hour

# Open Program to read and the specific file too
def openProgram():
    try:
        os.startfile("gamePrices.xlsx")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("Couldn't open file: " + str(e))

# Sheet Assignments
if os.path.exists("gamePrices.xlsx"):
    try:
        book = openpyxl.load_workbook("gamePrices.xlsx")
    except Exception as e:
        print(str(e))
        print("Couldn't open existing file. Creating new file.")
        book = openpyxl.load_workbook("gamePrices.xlsx")
else:
    book = openpyxl.Workbook()

sheet = book.active

# Only write the headers if the file is new (organization)
if not os.path.exists("gamePrices.xlsx"):
    sheet["A1"] = "Game"
    sheet["B1"] = "Site"
    sheet["C1"] = "Price"

# Array/List assignments
siteList = []
gameList = []

# Warning before execution
def disclose():
    print("This program compares game prices between websites.")
    print("Provide sites that show game titles AND prices.")
    print("Sites requiring login will not work.\n")

'''
Sample sites
playstation store 
EB Games
'''

# Fixed non functional loop here too
# Asks the user to enter one or more websites to scrape
def siteInput():
    while True:
        site = input("Enter a website: ")
        siteList.append(site)
        print("Added " + site + " to the list.")
        print("Would you like to add another? (Y/N)")
        if input().strip().upper() == "N":
            break

# Fixed non functional loop 
# Asks the user to enter one or more game titles to search for
def gameInput():
    while True:
        game = input("Enter a game title: ")
        gameList.append(game)
        print("Added " + game + " to the list.")
        print("Would you like to add another? (Y/N)")
        if input().strip().upper() == "N":
            break

# Gouged the Regex logic. kept bugging me that its too advanced
# Scrapes a given website and returns the first price found near the game title
def scrapePrice(site, game):
    try:
        html = urllib.request.urlopen(site).read()
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text()
    except Exception as e:
        print("Could not reach " + site + ": " + str(e))
        return "Error reaching site"

    if game.lower() not in text.lower():
        return "Some games may not have been found in site selection."

    words = text.split()
    for word in words:
        if word[0] == "$" and len(word) > 1:
            return word.replace(",", "")
    return "No price found"


# Writes each result to the spreadsheet and saves the file
def writeToExcel(results):
    row = 2
    for game, site, price in results:
        sheet.cell(row=row, column=1).value = game
        sheet.cell(row=row, column=2).value = site
        sheet.cell(row=row, column=3).value = price
        row += 1
    try:
        book.save("gamePrices.xlsx")
        print("Results saved to gamePrices.xlsx")
    except PermissionError:
        print("Close the Excel file first. Could not save.")

# Program Execution
disclose() # Warning and explanation
siteInput() # Websites
gameInput() # Game Names

# Week long run time is probablt a bad idea but if this is for my gf then I can leave my main pc on that long 
endDate = datetime.datetime.now() + datetime.timedelta(days=7) # DELTA DELTA DELTA

# Run until the end of the week
while datetime.datetime.now() < endDate:
    results = []

    # Loop through every game/site combination and scrape the price 
    for game in gameList:
        for site in siteList:
            price = scrapePrice(site, game)
            results.append([game, site, price]) # Allowed method ^assignment

    writeToExcel(results)
    openProgram() # Open the program probably excel assume C: drive
    print("Results saved to gamePrices.xlsx")

    # wait fo r site refresh
    refresh()