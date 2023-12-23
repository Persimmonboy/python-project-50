import pytest
from gendiff.cli import main
from unittest.mock import patch

FIXTURES_DIR = 'tests/fixtures'

def get_file_path(filename):
    return f'{FIXTURES_DIR}/{filename}'

FILE1 = get_file_path('file1.json')
FILE2 = get_file_path('file2.json')

def read_expected_output(filename):
    with open(get_file_path(filename), 'r') as file:
        return file.read().strip()

@pytest.mark.parametrize("args, expected_file", [
    ([FILE1, FILE2], 'expected_stylish_result.txt'),
    ([FILE1, FILE2, '--format', 'stylish'], 'expected_stylish_result.txt'),
    ([FILE1, FILE2, '--format', 'plain'], 'expected_plain_result.txt'),
    ([FILE1, FILE2, '--format', 'json'], 'expected_json_result.json'),
])
def test_cli(args, expected_file):
    expected_output = read_expected_output(expected_file)
    with patch('sys.argv', ['gendiff'] + args):
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_with(expected_output)

def test_cli_error():
    with patch('sys.argv', ['gendiff', 'nonexistent.json', FILE2]):
        with patch('sys.exit') as mock_exit:
            main()
            mock_exit.assert_called()
