import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='''
    Compares two configuration files and shows a difference.''')
    parser.add_argument("file1", type=str, help="first_file")
    parser.add_argument("file2", type=str, help="second_file")
    parser.add_argument('-f', '--format', help='set format of output')
    return parser.parse_args()
