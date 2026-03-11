"""

"""


import urllib.request
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
webUrl = urllib.request.urlopen(url)
html = webUrl.read()

soup = BeautifulSoup(html, 'html.parser')
displayedText = soup.get_text()
words = displayedText.split()

quotes = []
authors = []

"""
pullQuotes() function iterates through the list of words and collects sequences of words that start with “ and end with ” as quotes. 
It uses a while loop to gather all the words in between and then joins them together, stripping the fancy quotes.
"""
def pullQuotes():
    i = 0
    while i < len(words):
        if words[i].startswith("“"):
            quote_words = []

            # collect words until one ends with ”
            while i < len(words):
                quote_words.append(words[i])
                if words[i].endswith("”"):
                    break
                i += 1

            # join and strip the fancy quotes
            quote = " ".join(quote_words).strip("“”")
            quotes.append(quote)

        i += 1

def pullAuthors():
    i = 0
    while i < len(words):
        if words[i] == "by":
            name_parts = []
            j = i + 1

            # collect name parts until we hit "(about)" or "Tags:"
            while j < len(words) and words[j] not in ["(about)", "Tags:"]:
                name_parts.append(words[j])
                j += 1

            authors.append(" ".join(name_parts))
        i += 1

pullQuotes()
pullAuthors()

file = open("quotes.txt", "w")
for i in range(len(quotes)):
    file.write("\"" + quotes[i] + "\"")
    file.write("\n - " + authors[i] + "\n\n")
file.close()
