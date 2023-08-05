import pytest
import os
from gendiff.generate_diff import generate_diff
from gendiff.formatter import format_stylish

FIXTURES_DIR = os.path.join('tests', 'fixtures')

def get_file_path(filename):
    return os.path.join(FIXTURES_DIR, filename)

@pytest.mark.parametrize("file1_name, file2_name, expected_result_name", [
    ("file1.json", "file2.json", "expected_result.txt"),
    ("file1.yaml", "file2.yaml", "expected_result.txt"),
    ("file1_recursive.json", "file2_recursive.json", "expected_result_recursive.txt"),
])
def test_generator_diff(file1_name, file2_name, expected_result_name):
    file1_path = get_file_path(file1_name)
    file2_path = get_file_path(file2_name)
    expected_result_path = get_file_path(expected_result_name)

    with open(expected_result_path) as f:
        expected_result = f.read()

    diff = generate_diff(file1_path, file2_path)
    generated_diff = format_stylish(diff)
    assert generated_diff == expected_result

def test_empty_files():
    empty_file_path = get_file_path('empty_file.json')
    diff = generate_diff(empty_file_path, empty_file_path)
    formatted_diff = format_stylish(diff)
    assert formatted_diff == '{\n\n}'
