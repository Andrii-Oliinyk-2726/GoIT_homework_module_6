import os
import sys
import shutil
from pathlib import Path
# & C:/Python_3.10.9/python.exe "d:/_GoIT/Python 11/module_6_HW_v1.py" "d:/_GoIT/Python 11/Trash_hw_module_6"
folder_path = sys.argv[1]
# folder_path = r'D:\_GoIT\Python 11\Trash_hw_module_6'
# folder_move = r'D:\_GoIT\Python 11\Trash_hw_module_6'
folder_move = sys.argv[1]
folder_names = ['images', 'video', 'documents', 'audio', 'archives', 'others']
images_format = ['jpg', 'jpeg', 'png', 'svg', 'bmp']
video_format = ['avi', 'mp4', 'mov', 'mkv', 'mpeg', 'mpg', 'flac']
documents_format = ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'xls', 'pptx']
audio_format = ['mp3', 'ogg', 'wav', 'amr']
archives_format = ['zip', 'gz', 'tar']
folder_familiar_suffixes = []
folder_unfamiliar_suffixes = []

# translation file_name
def normalize(name):
    map = {ord('а'): 'a', ord('б'): 'b', ord('в'): 'v', ord('г'): 'g',
           ord('д'): 'd', ord('е'): 'e', ord('ж'): 'j', ord('з'): 'z',
           ord('и'): 'i', ord('й'): 'j', ord('к'): 'k', ord('л'): 'l',
           ord('м'): 'm', ord('н'): 'n', ord('о'): 'o', ord('п'): 'p',
           ord('р'): 'r', ord('с'): 's', ord('т'): 't', ord('у'): 'u',
           ord('ф'): 'f', ord('х'): 'h', ord('ц'): 'ts', ord('ч'): 'ch',
           ord('ш'): 'sh', ord('щ'): 'sch', ord('ъ'): '_', ord('ы'): 'e',
           ord('ь'): '_', ord('э'): 'e', ord('ю'): 'yu', ord('я'): 'ya',
           ord('є'): 'je', ord('і'): 'i', ord('ї'): 'ji', ord('ґ'): 'g',
           ord('A'): 'A', ord('Б'): 'B', ord('В'): 'V', ord('Г'): 'G',
           ord('Д'): 'D', ord('Е'): 'E', ord('Ж'): 'J', ord('З'): 'Z',
           ord('И'): 'I', ord('Й'): 'J', ord('К'): 'K', ord('Л'): 'L',
           ord('М'): 'M', ord('Н'): 'N', ord('О'): 'O', ord('П'): 'P',
           ord('Р'): 'R', ord('С'): 'S', ord('Т'): 'T', ord('У'): 'U',
           ord('Ф'): 'F', ord('Х'): 'H', ord('Ц'): 'TS', ord('Ч'): 'CH',
           ord('Ш'): 'SH', ord('Щ'): 'SCH', ord('Ъ'): '_', ord('Ы'): 'E',
           ord('Ь'): '_', ord('Э'): 'E', ord('Ю'): 'YU', ord('Я'): 'YA',
           ord('Є'): 'JE', ord('І'): 'I', ord('Ї'): 'JI', ord('Ґ'): 'G',
           ord('#'): '_'
           }
    return name.translate(map)


# create folder_names for out result
def create_folders_from_list(folder_path, folder_names):
    for folder in folder_names:
        if not os.path.exists(f'{folder_path}\\{folder}'):
            os.mkdir(f'{folder_path}\\{folder}')

# enumeration, sorting, count familiar/unfamiliar suffexes, unpacking archives 
def enumeration_Files(path):
    for i in os.listdir(path):
        if i in folder_names:
            continue
        if os.path.isdir(path + '\\' + i):
            enumeration_Files(path + '\\' + i)
        else:
            p = Path(path + '\\' + i)
            sfx = p.suffix
            if sfx[1:].lower() in images_format:
                if not sfx[1:] in folder_familiar_suffixes:
                    folder_familiar_suffixes.append(sfx[1:])
                file = path + "/" + i
                new_path = folder_move + "/images/" + i
                shutil.move(file, new_path)
            elif sfx[1:].lower() in video_format:
                if not sfx[1:] in folder_familiar_suffixes:
                    folder_familiar_suffixes.append(sfx[1:])
                file = path + "/" + i
                new_path = folder_move + "/video/" + i
                shutil.move(file, new_path)
            elif sfx[1:].lower() in documents_format:
                if not sfx[1:] in folder_familiar_suffixes:
                    folder_familiar_suffixes.append(sfx[1:])
                file = path + "/" + i
                new_path = folder_move + "/documents/" + i
                shutil.move(file, new_path)
            elif sfx[1:].lower() in audio_format:
                if not sfx[1:] in folder_familiar_suffixes:
                    folder_familiar_suffixes.append(sfx[1:])
                file = path + "/" + i
                new_path = folder_move + "/audio/" + i
                shutil.move(file, new_path)
            elif sfx[1:].lower() in archives_format:
                if not sfx[1:] in folder_familiar_suffixes:
                    folder_familiar_suffixes.append(sfx[1:])
                file = path + "/" + i
                new_path = folder_move + "/archives/" + i
                shutil.move(file, new_path)
                shutil.unpack_archive(folder_move + "/archives/" + i, folder_move + "/archives/") 
            else:
                if not sfx[1:] in folder_unfamiliar_suffixes:
                    folder_unfamiliar_suffixes.append(sfx[1:])
                file = path + "/" + i
                new_path = folder_move + "/others/" + i
                shutil.move(file, new_path)

# def for translation file names
def enumeration_Files_normalizate(path):
    for i in os.listdir(path):
        if os.path.isdir(path + '\\' + i):
            enumeration_Files_normalizate(path + '\\' + i)
        else:
            p = Path(path + '\\' + i)
            old_name = p.name
            norm_name = normalize(old_name)
            p1 = os.path.join(path, old_name)
            p2 = os.path.join(path, norm_name)
            shutil.move(p1, p2)

# delete empty folders
def del_empty_dirs(path):
    for d in os.listdir(path):
        a = os.path.join(path, d)
        if os.path.isdir(a):
            del_empty_dirs(a)
            if not os.listdir(a):
                os.rmdir(a)
                print(a, "deleted")

            
create_folders_from_list(folder_path, folder_names)
enumeration_Files(folder_path)
enumeration_Files_normalizate(folder_path)
del_empty_dirs(folder_path)
print("Ok")
print("Folder_familiar_suffixes = ", folder_familiar_suffixes)
print("Folder_unfamiliar_suffixes = ", folder_unfamiliar_suffixes)