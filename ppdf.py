import pdfplumber

# x8Path = '/Users/mrok/Downloads/x8.pdf'
# pythonPath = '/Users/mrok/Downloads/pypy.pdf'
# pdf_mt = pdfplumber.open(pythonPath)
# all_pages = pdf_mt.pages
# for pdf_pg in all_pages[156:157]:
#     print(pdf_pg.extract_text())
# for pdf_pg in all_pages[0:10]:
#     print(pdf_pg.extract_tables())


# import io
# import pytesseract
# import sys
 
# from PIL import Image
# from tika import parser
# from wand.image import Image as wi
 
# text_raw = parser.from_file(x8Path)
# print(text_raw['content'].strip())

li = []
[li.append(i) for i in range(10, 51)]
print(str(li))
print(li[0], li[-1])
