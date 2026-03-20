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
import os

# Potential violations ( Need to check if we ever learned os)
if os.path.exists("gameP[rices.xlsx"):
    book = openpyxl.load_workbook("gamePrices.xlsx")
else:
    book = openpyxl.Workbook()

# Sheet Assignments
sheet = book.active
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

# Asks user for a website(s)
def siteInput():
    siteCheck = False
    while siteCheck == False:
        site = input("Enter a website: ")
        siteList.append(site)
        print("Added " + site + " to the list.")
        print("Would you like to add another? (Y/N)")
        if input() == "N":
            siteCheck = True
        else:
            siteCheck = False
    

# Asks user for a game(s)
def gameInput():
    gameCheck = False
    while gameCheck == False:
        game = input("Enter a game title: ")
        gameList.append(game)

# Function to scrape a website for pricetags
def scrapePrice(site, game):
    try:
        html = urllib.request.urlopen(site).read()
        soup = BeautifulSoup(html, "html.parser")

        # VERY simple example: look for the game name and a price near it
        text = soup.get_text()

        if game.lower() not in text.lower():
            return "Not found"

        # naive price search
        import re
        prices = re.findall(r"\$\d+\.\d{2}", text)
        return prices[0] if prices else "No price found"

    except Exception as error:
        return "Error: " + str(error)

def writeToExcel(results):
    row = 2
    for game, site, price in results:
        sheet.cell(row=row, column=1).value = game
        sheet.cell(row=row, column=2).value = site
        sheet.cell(row=row, column=3).value = price
        row += 1

    book.save("gamePrices.xlsx")

# Program flow
disclose()
siteInput()

for i in range(2):
    gameInput()

results = []

for game in gameList:
    for site in siteList:
        price = scrapePrice(site, game)
        results.append((game, site, price))

writeToExcel(results)

print("Results saved to game_prices.xlsx")