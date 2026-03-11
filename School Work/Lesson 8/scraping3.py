import urllib.request
from bs4 import BeautifulSoup

url = "https://sandbox.oxylabs.io/products" # demo website for web scraping

webUrl = urllib.request.urlopen(url)
html = webUrl.read()
soup = BeautifulSoup(html, 'html.parser')

displayedText = soup.get_text() # Gets the text from the webpage
words = displayedText.split() # Splits the text into individual words

games = [] # Game list on certain platforms
price = [] # Price list for each game ( in Euros)






def output():
    file = open("game_prices.txt", "w")
    file.write("Games and their prices:\n")
    for i in range(len(games)):
        file.write(games[i] + " - " + price[i] + "\n")
    file.close()
