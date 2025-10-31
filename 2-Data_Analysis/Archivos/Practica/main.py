import os 
import shutil
from variables import *


doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif')
software_types = ('.exe', '.py','.ipynb')

ruta = os.path.join(os.getcwd(),ruta_base)

os.chdir(ruta)
os.mkdir("Imagenes")
os.mkdir("Documentos")
os.mkdir("Software")
os.mkdir("Otros")

for archivo in os.listdir(ruta):
    if archivo.endswith(doc_types) : 
        shutil.move(archivo,"Documentos")
    elif archivo.endswith(img_types) : 
        shutil.move(archivo, "Imagenes")
    elif archivo.endswith(software_types):
        shutil.move(archivo, "Software")
    elif archivo not in ["Documentos","Imagenes","Software","Otros"]:
        shutil.move(archivo, "Otros")

            