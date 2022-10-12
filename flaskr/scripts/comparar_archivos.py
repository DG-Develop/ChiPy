import hashlib

from difflib import SequenceMatcher


def hash_file(filename1, filename2):
    
    h1 = hashlib.sha1()
    h2 = hashlib.sha1()
    
    with open(filename1, "rb") as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h1.update(chunk)
    
    with open(filename2, "rb") as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h2.update(chunk)
    
    return h1.hexdigest(), h2.hexdigest()


msg1, msg2 = hash_file('static/pdf/SALUD-022-033.pdf', 'static/pdf/SALUD-022-033 - copia.pdf')

if msg1 != msg2:
    print('Estos archivos no son identicos')
    print((SequenceMatcher(None, msg1, msg2).ratio()) * 100 ) 
else:
    print('Estos archivos son identicos')
    print((SequenceMatcher(None, msg1, msg2).ratio()) * 100 )