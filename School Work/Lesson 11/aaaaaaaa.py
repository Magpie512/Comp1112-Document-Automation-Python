import docx
doc = docx.Document("test.docx")
fullText = []

for words in doc.paragraphs:
    fullText.append(words.text)
print(fullText)
