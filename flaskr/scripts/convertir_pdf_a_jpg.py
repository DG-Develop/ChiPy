import os
from pdf2image import convert_from_path

saving_folder = 'process'
pages = convert_from_path(pdf_path='static/pdf/SALUD-022-033.pdf', poppler_path='flaskr/scripts/poppler-22.04.0/Library/bin')

for i in range(len(pages)):
    pages[i].save(os.path.join(saving_folder, 'page'+str(i)+'.jpg'), 'JPEG')