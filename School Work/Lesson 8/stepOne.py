import urllib.request
WebUrl = urllib.request.urlopen("http://www.google.com")
print(WebUrl.getcode())