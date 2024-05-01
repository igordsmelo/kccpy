import os
import shutil
from subprocess import call

from send2trash import send2trash as trash


############################################################ RUN THIS FIRST, TO GET THE FILES AND FOLDERS TO CONVERT
def list_files(fldr_pth, exclude_format='MOBI') -> list:
    """
    List manga sub-folders/files in folder, returning them in a list. Excludes .MOBI files by default.
    :param fldr_pth:
    :param exclude_format:
    :return:
    """
    return [f"{fldr_pth}\\{f}" for f in os.listdir(fldr_pth) if exclude_format.lower() not in f]


############################################################ RUN THIS SECOND, TO CONVERT THEM
def convert(*files, ext='MOBI', output=None, fname=None, delete_original: bool = False) -> None:
    """
    Converts .CBZ/.CBR files to Kindle-adapted .MOBI file (by default). Check KCC's support for other formats.
    :param file:
    :param ext:
    :param output:
    :param fname:
    :param delete_original:
    """
    for file in files:
        output = f'--output="{output}"' if output else ''
        filename = f'--title="{fname}.{ext.lower()}"' if fname else ''
        call(f'kcc-c2e --profile=K578 -m --format={ext} {filename} {output} "{file}"')
        if delete_original:
            trash(file)


def make_comic(*files):
    """
    :param files: path to folders or that will, by default, be turned in .MOBI files.
    """
    for file in files:
        # print(file)
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
                convert(TEMP_FILE, fname=FILE_NAME)
            # FOR CBZ, RAR AND ZIP FILES...
            elif os.path.isfile(file) and any(ext in file for ext in ['.cbz', '.rar', '.zip']):
                TEMP_FILE = f'{TEMP}.{FILE_NAME.split(".")[-1]}'  # KCCPY_TEMP.cbz, KCCPY_TEMP.rar or KCCPY_TEMP.ZIP
                shutil.copy(file, TEMP_FILE)
                ###
                # TODO: it doesnt inherit the name, check to see if it can be done.
                convert(TEMP_FILE, fname=FILE_NAME)
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
