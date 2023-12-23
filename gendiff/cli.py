import argparse
import sys
from gendiff.generate_diff import generate_diff
from gendiff.formatter import format_stylish, format_plain, format_json


def parse_args():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument("file1", type=str, help="first_file")
    parser.add_argument("file2", type=str, help="second_file")
    parser.add_argument('-f', '--format',
                        help='set format of output',
                        choices=['stylish', 'plain', 'json'],
                        default='stylish')
    return parser.parse_args()


def main():
    try:
        args = parse_args()
        diff = generate_diff(args.file1, args.file2)

        if args.format == 'stylish':
            print(format_stylish(diff))
        elif args.format == 'plain':
            print(format_plain(diff))
        elif args.format == 'json':
            print(format_json(diff))
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
