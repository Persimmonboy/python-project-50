import argparse


def gendiff(file1, file2):
    pass


def main():
    parser = argparse.ArgumentParser(description='''
    Compares two configuration files and shows a difference.''')
    parser.add_argument("file1", type=str, help="second_file")
    parser.add_argument("file2", type=str, help="first_file")
    args = parser.parse_args()

    gendiff(args.file1, args.file2)


if __name__ == "__main__":
    main()
