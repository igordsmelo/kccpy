from subprocess import call
from send2trash import send2trash as trash
from os import listdir
from shutil import copy
from time import sleep
from utils.windows_tools import notification #todo: import this from DailyTasks


############################################################ RUN THIS FIRST, TO GET THE FILES AND FOLDERS TO CONVERT
def list_manga_files(fldr_pth, exclude_format='MOBI'):
    from os import listdir
    return [f"{fldr_pth}\\{f}" for f in listdir(fldr_pth) if exclude_format.lower() not in f]


############################################################ RUN THIS SECOND, TO CONVERT THEM
def make_manga(file, format='MOBI', output=None, fname=None, delete_original=True):
    output = f'--output="{output}" ' if output else ''
    filename = f'--title="{fname}.{format.lower()}" ' if fname else ''
    call(f'kcc-c2e --profile=K578 -m --format={format} {filename} {output}"{file}"')
    notification('manga converted')
    if delete_original:
        trash(file)


############################################################ PERSONAL WORKFLOW
############################################################ RUN THIS THIRD, TO GET THE FILES ON KINDLE
def send_to_kindle(file, kindle_dir="E:\\", delete_original=True):
    try:
        ############################################################# check if e\documents exist
        a = listdir(kindle_dir)
        ############################################################## check if a few folders are in E: root
        kindle = ['audible', 'documents', 'fonts', '.active_content_sandbox', 'driveinfo.calibre', 'metadata.calibre']
        ############################################################## sends file to kindle
        if all(x in a for x in kindle):
            copy(file, fr"{kindle_dir}documents")
            notification('file sent to kindle')
            sleep(3)
        if delete_original:
            trash(file)
    except FileNotFoundError:
        notification('file not found')
        pass


import os
path = r"D:\Users\Igor\Documents\Sync\Manga"
paths = [f"{path}\\{p}" for p in os.listdir(path) if os.path.isdir(f"{path}\\{p}")]
for p in paths:
    for manga in os.listdir(p):
        pth = f"{p}\\{manga}"
        if os.path.isdir(pth):
            chapters = os.listdir(pth)
            chapters.sort()  # tries to sort list alphabetically. Doesn't work perfectly. #todo: fix it.
            mobi_name = f"{manga} {chapters[0]}-{chapters[-1]}"
            if any('cbz' in c for c in chapters) or any('_tmp' in c for c in chapters):
                print(f'haha {manga} is wrong')
            else:
                print(f'converting {manga}')
                make_manga(pth, fname=mobi_name)
############################################################
