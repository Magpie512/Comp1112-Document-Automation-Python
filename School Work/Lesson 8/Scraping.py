"""
Mars Briggs
200561234
March 10th 2026
User enters the url to scrape book titles and prices, and competitors price then print to a file
https://books.toscrape.com/catalogue/category/books/young-adult_21/page-2.html
"""

import urllib.request
from bs4 import BeautifulSoup

# User Input suppliments
url = "https://books.toscrape.com/catalogue/category/books/young-adult_21/page-2.html"
bookTitle = "The Alien Club"
ourPrice = "£51.77"

WebUrl = urllib.request.urlopen(url)
html = WebUrl.read()

soup = BeautifulSoup(html, 'html.parser')
displayedText = soup.get_text()
words = displayedText.split()

compPrice = None

# detect a price  like £51.77
def checkPrice(price):
    if len(price) > 1 and price[0] == '£': # EURO
        remainder = price[1:]
        digits = "0123456789."
        for char in remainder:
            if char not in digits:
                return False
        return True
    return False

# Title Compounding
titleWords = bookTitle.split()
titleLen = len(titleWords)

# Loop for finding the Title
for i in range(len(words) - titleLen):
    # Rebuild a Title of equal length
    phrase = " ".join(words[i:i + titleLen])

    # Compare to user input
    if phrase.lower() == bookTitle.lower():
        # After a title, the next price appears shortly after in the text
        for j in range(i, len(words)):
            if checkPrice(words[j]):
                compPrice = words[j]
                break
        break

# Write results to file
if compPrice:
    file = open("book_prices.txt", "w")
    file.write("Title: " + bookTitle + " | Your Price: " + ourPrice + " | Competitor's Pricing: " + compPrice)
    file.close()
else:
    print("Book not found on competitor site.")
