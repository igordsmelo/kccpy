import kccpy.utils as kcc


def main() -> None:
    file = input('Paste path to file here')
    kcc.make_comic(file)
    print('Conversion finished. Enjoy your reading!')


if __name__ == '__main__':
    main()
