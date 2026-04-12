import PyPDF2, time

file = open('School Work/Lesson 12/ThePDF.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(file)

def decrypt6():
    pdfReader.decrypt('abcdab')

if pdfReader.is_encrypted:
    decrypt6()

pdfPage = pdfReader.pages[0]
print(pdfPage.extract_text())
