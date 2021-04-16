import os
import shutil
from zipfile import ZipFile

__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

# Optioneel arg toevoegen vond ik er beter uitzien, zeker icm cache_zip()
def clean_cache(chache_dir_path='cache'):
    
    # Als folder al bestaan, dan geheel verwijderen en nieuwe maken
    if os.path.exists(chache_dir_path):
        shutil.rmtree(chache_dir_path)
        os.mkdir(chache_dir_path)
    else:
        # Als folder nog niet bestaat, maken
        os.mkdir(chache_dir_path)

def cache_zip(zip_file_path, chache_dir_path):
    
    # Folder leegmaken, of aanmaken
    clean_cache(chache_dir_path)
    
    # Alle files in de zip in de folder uitpakken
    with ZipFile(zip_file_path, 'r') as zipObj:
        zipObj.extractall(chache_dir_path)
       
def cached_files(chache_dir_path='cache'):

    # Enkel het bovenste leven van de foldertree gebruiken, daarom een break
    for root, dirs, files in os.walk(chache_dir_path, topdown=True):
        list_of_files_rel = files
        break
    
    # Root toevoegen, waar de files stonden
    list_of_files_root = [os.path.join(root, file) for file in list_of_files_rel]

    # Van relatieve naar absolute paths gaan
    list_of_files_abs = [os.path.abspath(file) for file in list_of_files_root]

    return list_of_files_abs

def find_password(list_of_files_abs):

    # Elke file uit de lijst open en de regels afstruinen naar password
    for file in list_of_files_abs:
        with open(file) as f:
            for line in f:
                if 'password' in line:
                    # Als gevonden, dan password: en newline eraf halen
                    len_prefix = len('password: ')
                    line = line.strip()
                    return line[len_prefix:]

if __name__ == '__main__':
    pass
    