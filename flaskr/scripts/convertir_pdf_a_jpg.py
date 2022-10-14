import os
from pdf2image import convert_from_path

saving_folder = 'process'
original_pages = convert_from_path(pdf_path='static/pdf/SALUD-022-033.pdf', poppler_path='flaskr/scripts/poppler-22.04.0/Library/bin')
# actual_pages = convert_from_path(pdf_path='static/pdf/SALUD-022-033 - copia.pdf', poppler_path='flaskr/scripts/poppler-22.04.0/Library/bin')

for i in range(len(original_pages)):
    original_pages[i].save(os.path.join(saving_folder, 'original-page'+str(i)+'.jpg'), 'JPEG')
    
# for i in range(len(actual_pages)):
#     actual_pages[i].save(os.path.join(saving_folder, 'actual-page'+str(i)+'jpg'), 'JPEG')
    
