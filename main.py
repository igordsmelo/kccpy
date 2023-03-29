from os import listdir
from shutil import copy
from subprocess import call
from time import sleep

from send2trash import send2trash as trash

# sys.path.append(r'D:\Users\Igor\Documents\MEGA\Programming\Projects\DailyTasks')
a

############################################################ RUN THIS FIRST, TO GET THE FILES AND FOLDERS TO CONVERT
def list_manga_files(fldr_pth, exclude_format='MOBI'):
    from os import listdir
    return [f"{fldr_pth}\\{f}" for f in listdir(fldr_pth) if exclude_format.lower() not in f]


############################################################ RUN THIS SECOND, TO CONVERT THEM
def make_manga(file, format='MOBI', output=None, fname=None, delete_original=True):
    output = f'--output="{output}" ' if output else ''
    filename = f'--title="{fname}.{format.lower()}" ' if fname else ''
    call(f'kcc-c2e --profile=K578 -m --format={format} {filename} {output}"{file}"')
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
            sleep(3)
        if delete_original:
            trash(file)
    except FileNotFoundError:
        print('file not found')
        pass

############################################################

def main():
    from os.path import isdir  # checks if folder exists.
    from os import listdir  # gets files in dir.
    path = r"D:\Users\Igor\Documents\Sync\Manga"
    paths = [f"{path}\\{p}" for p in listdir(path) if isdir(f"{path}\\{p}")]
    for p in paths:
        for manga in listdir(p):
            pth = f"{p}\\{manga}"
            if isdir(pth):
                chapters = listdir(pth)
                chapters.sort()  # tries to sort list alphabetically. Doesn't work perfectly. #TODO: fix it.
                mobi_name = f"{manga} {chapters[0]}-{chapters[-1]}"
                if any('cbz' in c for c in chapters) or any('_tmp' in c for c in chapters):
                    print(f'haha {manga} is wrong')
                else:
                    print(f'converting {manga}')
                    make_manga(pth, fname=mobi_name)


############################################################

if __name__ == '__main__':
    main()
