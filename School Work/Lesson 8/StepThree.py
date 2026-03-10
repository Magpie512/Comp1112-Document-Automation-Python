#Utilizing beautiful soup to parse the data from google.com
import urllib.request
from bs4 import BeautifulSoup

WebUrl = urllib.request.urlopen("http://www.barrie.ca")
html = WebUrl.read()

soup = BeautifulSoup(html, 'html.parser')
displayedText = soup.get_text()
listOfDisplayedText = displayedText.split()

for word in listOfDisplayedText:
    digits = '0123456789'
    count = 0
    for i in range(len(word)):
        if word[i] in digits:
            count += 1
    if count== 10:
        print(word)
    else:
        pass