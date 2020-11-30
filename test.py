from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import os
from pathlib import Path

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\winMark\AppData\Local\Tesseract-OCR\tesseract.exe'

pdf_file = Path.cwd() / "test2.pdf"

pages = convert_from_path(pdf_file)

image_counter = 1

for page in pages:
    filename = 'page_' + str(image_counter) + ".jpg"

    page.save(filename, 'JPEG')

    image_counter = image_counter + 1

filelimit = image_counter-1

outfile = 'out_text.txt'

f = open(outfile, 'a', encoding='utf-8')

for i in range(1, filelimit + 1):
    filename = 'page_'+str(i)+'.jpg'

    text = str(pytesseract.image_to_string(Image.open(filename), 'rus'))

    # text = text.replace('-\n', '')

    f.write(text)

f.close()