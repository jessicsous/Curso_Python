# OS + SHUTIL - mover, copiar e apagar arquivos

import os
import shutil

caminho_original = r'C:\Users\desou\OneDrive\Documentos\GitHub\videos'
caminho_novo = r'C:\Users\desou\OneDrive\Documentos\GitHub\videos3'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'pasta já existe')

for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        if '.str' in file:
            shutil.copy(old_file_path, new_file_path) # copiar
            print(f'arquivo {file} movido')

