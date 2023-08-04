from gendiff import cli
from gendiff import generate_diff

def main():
    args = cli.parse_args()
    diff = generate_diff.generate_diff(args.file1, args.file2)
    print(diff)

if __name__ == "__main__":
    main()
