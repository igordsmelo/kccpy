from os import listdir
from subprocess import call

from send2trash import send2trash as trash


############################################################ RUN THIS FIRST, TO GET THE FILES AND FOLDERS TO CONVERT
def list_manga_files(fldr_pth, exclude_format='MOBI') -> list:
    """
    List manga sub-folders/files in folder, returning them in a list. Excludes .MOBI files by default.
    :param fldr_pth:
    :param exclude_format:
    :return:
    """
    return [f"{fldr_pth}\\{f}" for f in listdir(fldr_pth) if exclude_format.lower() not in f]


############################################################ RUN THIS SECOND, TO CONVERT THEM
def make_manga(*files, ext='MOBI', output=None, fname=None, delete_original=False):
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



