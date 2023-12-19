import os.path
import shutil, os

import WIP.script_kccpy.utils as kcc

folder = r"B:\3\Mangas\ワンピース 第01-94巻 [ONE PIECE vol 01-94]"
manga_files = kcc.list_manga_files(folder)


def main(*files):
    """
    :param files: path to folders or files
    """
    for file in files:
        print(file)
        file = str(file)
        FILE_PARENT = '\\'.join(file.split('\\')[:-1])  # B:\3\Mangas\ワンピース 第01-94巻 [ONE PIECE vol 01-94]
        FILE_NAME = file.split('\\')[-1].split('.')[0]  # [尾田栄一郎] ONE PIECE 第01巻
        TEMP = f"KCCPY_TEMP"
        ###
        if not os.path.exists(f"{FILE_PARENT}\\{FILE_NAME}.mobi") and os.path.exists(file):
            # FOR FOLDERS
            if os.path.isdir(file):
                shutil.make_archive(TEMP, 'zip', FILE_PARENT, FILE_NAME)
                print('ZIP created. Converting to .MOBI now:\n\n')
                TEMP_FILE = f'{TEMP}.zip'
                ###
                # TODO: it doesnt inherit the name, check to see if it can be done.
                kcc.make_manga(TEMP_FILE, fname=FILE_NAME)
            # FOR CBZ, RAR AND ZIP FILES...
            elif os.path.isfile(file) and any(ext in file for ext in ['.cbz', '.rar', '.zip']):
                TEMP_FILE = f'{TEMP}.{FILE_NAME.split(".")[-1]}'  # KCCPY_TEMP.cbz, KCCPY_TEMP.rar or KCCPY_TEMP.ZIP
                shutil.copy(file, TEMP_FILE)
                ###
                # TODO: it doesnt inherit the name, check to see if it can be done.
                kcc.make_manga(TEMP_FILE, fname=FILE_NAME)
            ###
            try:
                os.rename(f'{TEMP}.mobi', f'{FILE_NAME}.mobi')
                shutil.move(f'{FILE_NAME}.mobi', FILE_PARENT)
                os.remove(TEMP_FILE)
                print(f'\n\n{FILE_NAME}.mobi is complete.')
            except FileNotFoundError:
                pass
        else:
            print(f"'file: {FILE_PARENT}\\{FILE_NAME}.mobi'\n already exists, skipping...\n\n")


if __name__ == '__main__':
    main(manga_files[13])
