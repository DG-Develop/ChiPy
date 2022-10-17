import os
from pdf2image import convert_from_path
# import cv2
# import imutils


saving_folder = 'process'
original_pages = convert_from_path(pdf_path='static/pdf/SAFIN-022-067.pdf', poppler_path='flaskr/scripts/poppler-22.04.0/Library/bin')
actual_pages = convert_from_path(pdf_path='static/pdf/SAFIN-022-067 escaneado.pdf', poppler_path='flaskr/scripts/poppler-22.04.0/Library/bin')

numero_pagina_original = len(original_pages)
numero_pagina_actual = len(actual_pages)

for i in range(numero_pagina_original):
    filename = os.path.join(saving_folder, 'original-page'+str(i)+'.png')
    
    if os.path.exists(filename):
        continue
    
    original_pages[i].save(filename, 'PNG')
    
for i in range(numero_pagina_actual):
    filename = os.path.join(saving_folder, 'actual-page'+str(i)+'.png')
    
    if os.path.exists(filename):
        continue
    
    actual_pages[i].save(filename, 'PNG')
    

# pyteseract
from PIL import Image
from pytesseract import pytesseract

path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image_path = 'process/actual-page0.png'

img = Image.open(image_path)

pytesseract.tesseract_cmd = path_to_tesseract

text = pytesseract.image_to_string(img)

with open(os.path.join(saving_folder,'texto-page0.txt'),'w') as f: 
    f.write(str(text))

# OpenCV
# for i in range(numero_pagina_original):   
#     original = cv2.imread(f'process/original-page{i}.png')
#     new = cv2.imread(f'process/actual-page{i}.png')

#     original = imutils.resize(original, height=600)
#     new = imutils.resize(new, height=600)

#     diff = original.copy()
#     cv2.absdiff(original, new, diff)

#     gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

#     for j in range(0, 3):
#         dilated =  cv2.dilate(gray.copy(), None, iterations=j+1)
    

#     (T, thresh) = cv2.threshold(dilated, 3, 255, cv2.THRESH_BINARY)

#     cnts = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#     cnts = imutils.grab_contours(cnts)

#     for c in cnts:
#         (x,y,w,h) = cv2.boundingRect(c)
#         cv2.rectangle(new, (x,y), (x + w, y + h), (0, 255, 0), 2)
        
#     cv2.imwrite(f'process/change-page{i}.png', new)