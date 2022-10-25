import os
from pdf2image import convert_from_path
import cv2
import imutils
from PIL import Image, ImageFont, ImageDraw
from pytesseract import pytesseract
import numpy as np

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
    


def text_to_image(text: str):
    flag = False
    lista = list()
    for linea in text.split('\n'):
        if "No. SAFIN-022-067" in linea:
            flag = True
        
        if flag:
            lista.append(linea)
        
        
    lineas = tuple(lista)
    # lineas = tuple(linea.rstrip() for linea in text.split('\n'))
    
    font = ImageFont.truetype('static/fonts/QuatroSlab-Regular.ttf')
    teststr = 'abcefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZáéíóúÁÉÍÓÚ””'	
    pt2px = lambda pt: int(round(pt * 96.0 / 72))
    
    # Alto y Ancho  imagen
    # max_width_line = max(lineas, key=lambda s: font.getbbox(s)[2])
    # max_width_font = pt2px(font.getbbox(max_width_line)[2])
    max_height_font = pt2px(font.getbbox(teststr)[3])	
    # height = max_height_font * len(lineas)
    # width = int(round(max_width_font + 10))
    
    x = 10
    y = 10	
    image = Image.new('L', (690, 1000), color=255)
    draw = ImageDraw.Draw(image)	
	
    for sline in lineas:
        draw.text((x, y), sline, font=font)
        y += max_height_font
        
    image_array = np.array(image)
    ocvim = cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)
    
    return ocvim

# pyteseract

# No olvidar el .exe de tesseract para windows y en la ruta especificada
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    
for i in range(numero_pagina_original):
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
    

    # OpenCV
    imagen_original = text_to_image(text_original)
    imagen_nuevo = text_to_image(text_nuevo)
    
    diff = imagen_original.copy()
    cv2.absdiff(imagen_original, imagen_nuevo, diff)
    
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    for j in range(0, 3):
        dilated =  cv2.dilate(gray.copy(), None, iterations=j+1)
    
    (T, thresh) = cv2.threshold(dilated, 3, 255, cv2.THRESH_BINARY)

    cnts = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        (x,y,w,h) = cv2.boundingRect(c)
        cv2.rectangle(imagen_nuevo, (x,y), (x + w, y + h), (0, 255, 0), 2)
        
    cv2.imwrite(f'process/change-original-page{i}.png', imagen_original)
    cv2.imwrite(f'process/change-page{i}.png', imagen_nuevo)
    
    os.remove(f'process/original-page{i}.png')
    os.remove(f'process/actual-page{i}.png')