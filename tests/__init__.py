from os import listdir
from shutil import copy
from time import sleep

from send2trash import send2trash as trash


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