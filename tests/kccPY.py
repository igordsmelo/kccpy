from os import listdir
from subprocess import call

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
