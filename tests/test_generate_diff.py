import pytest
import json
import os
from gendiff.generate_diff import generate_diff
from gendiff.formatter import format_stylish, format_plain, format_json

FIXTURES_DIR = os.path.join('tests', 'fixtures')

def get_file_path(filename):
    return os.path.join(FIXTURES_DIR, filename)

@pytest.mark.parametrize("file1_name, file2_name, expected_result_name", [
    ("file1.json", "file2.json", "expected_stylish_result.txt"),
    ("file1.yaml", "file2.yaml", "expected_stylish_result.txt"),
    ("file1_recursive.json", "file2_recursive.json", "expected_stylish_recursive_result.txt"),
])
def test_format_stylish(file1_name, file2_name, expected_result_name):
    file1_path = get_file_path(file1_name)
    file2_path = get_file_path(file2_name)
    expected_result_path = get_file_path(expected_result_name)

    with open(expected_result_path) as f:
        expected_result = f.read().strip()

    diff = generate_diff(file1_path, file2_path)
    formatted_diff = format_stylish(diff)
    assert formatted_diff.strip() == expected_result

@pytest.mark.parametrize("file1_name, file2_name, expected_result_name", [
    ("file1.json", "file2.json", "expected_plain_result.txt"),
    ("file1.yaml", "file2.yaml", "expected_plain_result.txt"),
    ("file1_recursive.json", "file2_recursive.json", "expected_plain_recursive_result.txt"),
])
def test_format_plain(file1_name, file2_name, expected_result_name):
    file1_path = get_file_path(file1_name)
    file2_path = get_file_path(file2_name)
    expected_result_path = get_file_path(expected_result_name)

    with open(expected_result_path) as f:
        expected_result = f.read().strip()

    diff = generate_diff(file1_path, file2_path)
    formatted_diff = format_plain(diff)
    assert formatted_diff.strip() == expected_result

@pytest.mark.parametrize("file1_name, file2_name, expected_result_name", [
    ("file1.json", "file2.json", "expected_json_result.json"),
    ("file1.yaml", "file2.yaml", "expected_json_result.json"),
    ("file1_recursive.json", "file2_recursive.json", "expected_json_recursive_result.json"),
])
def test_format_json(file1_name, file2_name, expected_result_name):
    file1_path = get_file_path(file1_name)
    file2_path = get_file_path(file2_name)
    expected_result_path = get_file_path(expected_result_name)

    with open(expected_result_path) as f:
        expected_result = json.load(f)

    diff = generate_diff(file1_path, file2_path)
    formatted_diff = format_json(diff)
    assert json.loads(formatted_diff) == expected_result

def test_empty_files():
    empty_file_path = get_file_path('empty_file.json')
    diff = generate_diff(empty_file_path, empty_file_path)
    formatted_diff = format_stylish(diff)
    assert formatted_diff == '{\n\n}'

def test_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        generate_diff('nonexistent_file.json', 'file2.json')
