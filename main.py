import utils


def main() -> None:
    file = input('Paste path to file here')
    utils.make_comic(file)
    print('Conversion finished. Enjoy your reading!')


if __name__ == '__main__':
    main()
