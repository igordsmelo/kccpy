from utils.utils import make_manga


# sys.path.append(r'D:\Users\Igor\Documents\MEGA\Programming\Projects\DailyTasks')

############################################################ RUN THIS FIRST, TO GET THE FILES AND FOLDERS TO CONVERT


############################################################ RUN THIS SECOND, TO CONVERT THEM

############################################################ PERSONAL WORKFLOW
############################################################ RUN THIS THIRD, TO GET THE FILES ON KINDLE

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
