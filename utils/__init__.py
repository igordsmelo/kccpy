from os import listdir
from shutil import copy
from subprocess import call
from time import sleep

from send2trash import send2trash as trash


class KCCPY:
    """Simplifying the automation of KCC's library"""
    def __init__(self):
        self.files: str or list = None
        self.files_directory: str = None

    def get_files(self, folder_path, exclude_format='MOBI') -> list:
        """
        List manga sub-folders/files in folder, returning them in a list. Excludes .MOBI files by default.
        :param folder_path: path to files or subfolders.
        :param exclude_format:
        :return:
        """
        self.files_directory = folder_path
        self.files = [f"{folder_path}\\{f}" for f in listdir(folder_path) if exclude_format.lower() not in f]

    def convert_to_comic(self, ext='MOBI', output=None, fname=None, delete_original=False):
        """
        Converts .CBZ/.CBR files to Kindle-adapted .MOBI file (by default). Check KCC's support for other formats.
        """
        for file in self.files:
            output = f'--output="{output}"' if output else ''
            filename = f'--title="{fname}.{ext.lower()}"' if fname else ''
            call(f'kcc-c2e --profile=K578 -m --format={ext} {filename} {output}"{file}"')
            print(f'{file} converted.\n\n')
            if delete_original:
                trash(file)


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


############################################################ PERSONAL WORKFLOW
############################################################ RUN THIS THIRD, TO GET THE FILES ON KINDLE
# todo: this is too manual, improve it so it detects Kindle automatically, without having to specify what is it's name
def send_to_kindle(file, kindle_dir="E:\\", delete_original=True):
    """

    :param file:
    :param kindle_dir:
    :param delete_original:
    """
    try:
        ############################################################# check if e\documents exist
        a = listdir(kindle_dir)
        ############################################################## check if a few folders are in E: root
        kindle = ['audible', 'documents', 'fonts', '.active_content_sandbox', 'driveinfo.calibre', 'metadata.calibre']
        ############################################################## sends file to kindle
        if all(x in a for x in kindle):
            copy(file, fr"{kindle_dir}documents")
            sleep(3)
        if delete_original:
            trash(file)
    except FileNotFoundError:
        print('file not found')
        pass
############################################################
