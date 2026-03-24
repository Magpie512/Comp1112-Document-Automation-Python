"""
Mars Briggs
200561234
2026-03-20
Game Price Point comparisson (that aint spelled right)
"""
# For Web scraping
import urllib.request
from bs4 import BeautifulSoup
import openpyxl # For Excel
import os # Maybe remove if invalid. check with wayne

# Sheet Assignments
if os.path.exists("gamePrices.xlsx"):# check with wayne
    book = openpyxl.load_workbook("gamePrices.xlsx")
else:
    book = openpyxl.Workbook()

sheet = book.active

# Only write the headers if the file is new (organization)
if not os.path.exists("gamePrices.xlsx"):# check with wayne
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
    html = urllib.request.urlopen(site).read()
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text()

    # If the game title is not on the page, return early (not found)
    if game.lower() not in text.lower():
        return "Not found"

    # Splits the page text into words and looks for the first price starting with $
    words = text.split()
    for word in words: # Simpler logic from my assignment in class
        if word[0] == "$" and len(word) > 1:
            price = word.replace(",", "")
            return price
    return "No price found"

# Writes each result to the spreadsheet and saves the file
def writeToExcel(results):
    row = 2
    for game, site, price in results:
        sheet.cell(row=row, column=1).value = game
        sheet.cell(row=row, column=2).value = site
        sheet.cell(row=row, column=3).value = price
        row += 1

    book.save("gamePrices.xlsx")

# Program Execution
disclose() # Warning and explanation
siteInput() # Websites
gameInput() # Game Names

results = []

# Loop through every game/site combination and scrape the price 
for game in gameList:
    for site in siteList:
        price = scrapePrice(site, game)
        results.append([game, site, price]) # Allowed method ^assignment

writeToExcel(results)

# Style Guide fix
print("Results saved to gamePrices.xlsx")