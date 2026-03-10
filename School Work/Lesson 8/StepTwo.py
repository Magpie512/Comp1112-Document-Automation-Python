import urllib.request
WebUrl = urllib.request.urlopen("http://www.google.com")
print(WebUrl.getcode())
data = WebUrl.read()
print(data)