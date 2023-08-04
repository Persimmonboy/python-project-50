import argparse
import json


def generate_diff(file1, file2):

    with open(file1, 'r') as file1, open(file2, 'r') as file2:

        file1_data = json.load(file1)
        file2_data = json.load(file2)

        diff = {}
        keys_union = set(file1_data.keys()) | set(file2_data.keys())

        for key in sorted(keys_union):
            value1 = file1_data.get(key)
            value2 = file2_data.get(key)

            if value1 == value2:
                diff[f'  {key}'] = value1
            elif value1 is None:
                diff[f'+ {key}'] = value2
            elif value2 is None:
                diff[f'- {key}'] = value1
            else:
                diff[f'- {key}'] = value1
                diff[f'+ {key}'] = value2

        output = '{\n'
        for k, v in diff.items():
            output += f'  {k}: {v}\n'
        output += '}'
        return output


def main():
    parser = argparse.ArgumentParser(description='''
    Compares two configuration files and shows a difference.''')
    parser.add_argument("file1", type=str, help="first_file")
    parser.add_argument("file2", type=str, help="second_file")
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()

    generate_diff(args.file1, args.file2)


if __name__ == "__main__":
    main()
