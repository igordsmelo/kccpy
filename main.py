import utils


def main() -> None:
    file = input('Paste path to file here. It supports folders (containing imgs), .CBZ, .RAR AND .ZIP files:\n - ')
    utils.make_comic(file)
    print('Conversion finished. Enjoy your reading!')


if __name__ == '__main__':
    main()
