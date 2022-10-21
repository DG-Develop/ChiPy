import os
from pdf2image import convert_from_path
import cv2
import imutils
from PIL import Image, ImageSequence, ImageFont, ImageDraw, ImageOps
from pytesseract import pytesseract

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

# No olvidar el .exe de tesseract para windows y en la ruta especificada
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    
for i in range(numero_pagina_original):
    
    if i == 2:
        break
    
    original = cv2.imread(f'process/original-page{i}.png')
    nuevo = cv2.imread(f'process/actual-page{i}.png')
    
    #Recortando imagen
    original = original[250:1950, 40:1660]
    nuevo = nuevo[250:1950, 40:1660]

    # img = Image.open(image_path)
    img_original = Image.fromarray(original)
    img_nuevo = Image.fromarray(nuevo)

    pytesseract.tesseract_cmd = path_to_tesseract

    text_original = pytesseract.image_to_string(img_original, lang='spa')
    text_nuevo = pytesseract.image_to_string(img_nuevo, lang='spa')

    # with open(os.path.join(saving_folder,f'texto-original-page{i}.txt'),'w') as f: 
    #     f.write(str(text_original))
    
    # with open(os.path.join(saving_folder,f'texto-nuevo-page{i}.txt'),'w') as f: 
    #     f.write(str(text_nuevo))
    
    lines_original = tuple(linea.rstrip() for linea in text_original.split('\n'))
    
    # TODO: Obtener todos los caracteres diferentes dentro del contrato
    
    font = ImageFont.load_default()
    teststr = 'abcefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZáéíóúÁÉÍÓÚ””'	
    pt2px = lambda pt: int(round(pt * 96.0 / 72))
    
    max_width_line = max(lines_original, key=lambda s: font.getsize(s)[0])
    max_width_font = pt2px(font.getsize(max_width_line)[0])
    max_height_font = pt2px(font.getsize(teststr)[1])	
    height = max_height_font * len(lines_original)
    width = int(round(max_width_font + 10))
    
    x = 10
    y = 10	
    image = Image.new('L', (width, height), color=255)
    draw = ImageDraw.Draw(image)	
	
    for sline in lines_original:
        draw.text((x, y), sline, font=font)
        y += max_height_font
    
    image.save(f'texto-original-page{i}.png')


# def txt2img(txtfile, tiffile):
# 	with open(txtfile, encoding='windows-1255') as stxt:
# 		slines = tuple(line.rstrip() for line in stxt.readlines())

# 	font = ImageFont.load_default()	
# 	teststr = 'abcefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'	
# 	pt2px = lambda pt: int(round(pt * 96.0 / 72))
	
# 	max_width_line = max(slines, key=lambda s: font.getsize(s)[0])
# 	max_width_font = pt2px(font.getsize(max_width_line)[0])
# 	max_height_font = pt2px(font.getsize(teststr)[1])	
# 	height = max_height_font * len(slines)
# 	width = int(round(max_width_font + 10))
# 	linespacing = int(round(max_height_font * 1.0))
# 	x = 10
# 	y = 10	
# 	image = Image.new('L', (width, height), color=255)
# 	draw = ImageDraw.Draw(image)	
	
# 	for sline in slines:
# 		draw.text((x, y), sline, font=font)
# 		y += max_height_font
		
# 	image.save(tiffile)
# 	image.show()	
# 	return


# txt2img('txt2tif.py', 'test1.tiff')




# OpenCV
# for i in range(numero_pagina_original):   
#     original = cv2.imread(f'process/original-page{i}.png')
#     new = cv2.imread(f'process/actual-page{i}.png')
#     # original = imutils.resize(original, height=600)
#     # new = imutils.resize(new, height=600)
    
#     original = original[250:1950, 40:1660]
#     new = new[250:1950, 40:1660]

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