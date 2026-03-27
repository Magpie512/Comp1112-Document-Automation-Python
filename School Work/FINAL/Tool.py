"""
Mars Briggs
200561234
2026-03-27 4:10 PM
Game Price Point comparisson (that aint spelled right)
"""
import urllib.request # For Web scraping
from bs4 import BeautifulSoup # HTML parsing
import openpyxl # For Excel
import os # file operations
import datetime # Time Calculations
import time # Sleep wait function

if os.path.exists("gamePrices.xlsx"): # Check if the Excel file already exists on disk
    os.remove("gamePrices.xlsx") # Delete the old file to start fresh

priceBook = openpyxl.Workbook() # Create a brand new workbook
priceSheet = priceBook.active # Get the active sheet from the workbook

priceSheet["A1"] = "Game" # Label column A as Game
priceSheet["B1"] = "Site" # Label column B as Site
priceSheet["C1"] = "Price" # Label column C as Price

websiteList = [] # List to store user entered website URLs
gameTitleList = [] # List to store user entered game titles

# Function to wait for site refresh(or rather estimated refresh(real refresh could be 3am pst for all I know))
def refresh():
    now = datetime.datetime.now() # Gets the current time
    midnight = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(days=1) # Sets midnight by taking today's date and adding exactly one day
    while datetime.datetime.now() < midnight: # Loop until midnight is reached
        time.sleep(3600) # 3600 seconds = 1 hour

# Open Program to read and the specific file too
def openProgram():
    try:
        os.startfile("gamePrices.xlsx") # Launch the file with the OS default program
    except FileNotFoundError:
        print("File not found.") # Notify the user the file could not be found
    except Exception as openError:
        print("Couldn't open file: " + str(openError)) # Print error details

# Warning before execution
def disclose():
    print("This program compares game prices between websites.") # Print the program's purpose
    print("Provide sites that show game titles AND prices.") # Warn about site requirements
    print("Sites requiring login will not work.\n") # Warn that login-protected sites are unsupported

'''
Sample sites
playstation store 
EB Games ( so actually this wont work unless we use something we havent learned yet)
I was trying to find the game website i used before but holy christ i instead found a texas death penalty site. WHAT!!!
'''



# Asks the user to enter one or more websites to scrape
def siteInput():
    addingMore = True # Flag to control whether to keep asking for sites
    while addingMore: # Loop until user chooses to stop
        site = input("Enter a website: ").strip() # Ask the user to type a website URL
        websiteList.append(site) # Add the entered URL to the list
        print("Added " + site + " to the list.") # Confirm the site was added
        print("Would you like to add another? (Y/N)") # Ask if the user wants to continue
        if input().strip().upper() == "N": # Check if the user wants to stop
            addingMore = False # Set flag to False to exit the loop

# Asks the user to enter one or more game titles to search for
def gameInput():
    addingMore = True # Flag to control whether to keep asking for titles
    while addingMore: # Loop until user chooses to stop
        game = input("Enter a game title: ").strip() # Ask the user to type a game title
        gameTitleList.append(game) # Add the entered title to the list
        print("Added " + game + " to the list.") # Confirm the title was added
        print("Would you like to add another? (Y/N)") # Ask if the user wants to continue
        if input().strip().upper() == "N": # Check if the user wants to stop
            addingMore = False # Set flag to False to exit the loop

# Gouged the Regex logic. kept bugging me that its too advanced
# Scrapes a given website and returns the first price found near the game title
def scrapePrice(targetSite, targetGame):
    try:
        html = urllib.request.urlopen(targetSite).read() # Fetch raw HTML bytes from the target website
        soup = BeautifulSoup(html, "html.parser") # Parse the HTML with BeautifulSoup
        text = soup.get_text() # Extract all visible text from the parsed HTML
    except Exception as scrapeError:
        print("Could not reach " + targetSite + ": " + str(scrapeError)) # Notify user of the failed site
        return "Error reaching site" # Return error string for the spreadsheet

    if targetGame.lower() not in text.lower(): # Check if the game title appears on the page
        return "Game not found on this site." # Return not-found message if absent

    words = text.split() # Split page text into individual words for scanning
    for word in words: # Iterate through each word looking for a price
        if word[0] == "$" and len(word) > 1: # Check if the word is a price starting with $
            return word.replace(",", "") # Return the price with commas stripped
    return "No price found" # Fallback if no price was located on the page

# Resets the Excel file by deleting and recreating it with fresh headers
def resetExcel():
    global priceBook, priceSheet # Access the global workbook and sheet variables
    if os.path.exists("gamePrices.xlsx"): # Check if the file exists before trying to delete
        os.remove("gamePrices.xlsx") # Delete the existing file
    priceBook = openpyxl.Workbook() # Create a fresh workbook
    priceSheet = priceBook.active # Get the active sheet
    priceSheet["A1"] = "Game" # Re-label column A
    priceSheet["B1"] = "Site" # Re-label column B
    priceSheet["C1"] = "Price" # Re-label column C

# Writes each result to the spreadsheet and saves the file
def writeToExcel(resultsList):
    rowIndex = 2 # Start from row 2 to preserve the header row
    for game, site, price in resultsList: # Loop through each result in the list
        priceSheet.cell(row=rowIndex, column=1).value = game # Write game title to column A
        priceSheet.cell(row=rowIndex, column=2).value = site # Write site URL to column B
        priceSheet.cell(row=rowIndex, column=3).value = price # Write scraped price to column C
        rowIndex += 1 # Advance to the next row
    try:
        priceBook.save("gamePrices.xlsx") # Save the workbook to disk
        print("Results saved to gamePrices.xlsx") # Confirm successful save
    except PermissionError:
        print("Close the Excel file first. Could not save.") # Prompt user to close the file

# Program Execution
disclose() # Warning and explanation
input("press enter to continue") # Flush terminal buffer before taking user input
siteInput() # Websites
gameInput() # Game Names

endDate = datetime.datetime.now() + datetime.timedelta(days=7) # Week long run time, DELTA DELTA DELTA

# Run until the end of the week
while datetime.datetime.now() < endDate:
    cycleResults = [] # Create an empty list for this cycle's results

    for gameTitle in gameTitleList: # Loop through every game title
        for website in websiteList: # Loop through every website
            foundPrice = scrapePrice(website, gameTitle) # Scrape the price for this game/site combo
            cycleResults.append([gameTitle, website, foundPrice]) # Append the result to the list

    writeToExcel(cycleResults) # Write the results to Excel
    openProgram() # Open the program probably excel assume C: drive
    print("Results saved to gamePrices.xlsx") # Print a confirmation message
    refresh() # Wait for site refresh
    resetExcel() # Delete and recreate the file fresh for the next cycle