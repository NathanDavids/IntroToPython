import re

def file_extension(text):
    patterntxt = r'\.txt$'
    patterndocx = r'\.docx$'
    patternpdf = r'\.pdf$'
    patternjpg = r'\.jpg$'
    patterncsv = r'\.csv$'
    matchtxt = re.search(patterntxt, text)
    matchdocx = re.search(patterndocx, text)
    matchpdf = re.search(patternpdf, text)
    matchjpg = re.search(patternjpg, text)
    matchcsv = re.search(patterncsv, text)
    if matchtxt:
        return text + ' is a Text Document and can be opened using a Notepad'
    elif matchdocx:
        return text + ' is a Word Document and can be opened using MS Word'
    elif matchpdf:
        return text + ' is a PDF Document and can be opened using Adobe PDF Reader'
    elif matchjpg:
        return text + ' is a Image Document and can be opened using Windows Image Viewer'
    elif matchcsv:
        return text + ' is a Comma-Separated Values Document and can be opened using Microsoft Excel'
    else:
        return 'No file type found'
    
text = input('Enter any text: ')
result = file_extension(text)
print(result)