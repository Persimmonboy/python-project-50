import os
import pytest
import json
from gendiff.parser import get_file_extension, parse_file


FIXTURES_DIR = os.path.join('tests', 'fixtures')


def get_file_path(filename):
    return os.path.join(FIXTURES_DIR, filename)


@pytest.mark.parametrize("file_name, expected_extension", [
    ("file1.json", 'json'),
    ("file1.yml", 'yml'),
    ("file2.yaml", 'yaml')
])
def test_get_file_extension(file_name, expected_extension):
    file_path = get_file_path(file_name)
    file_extension = get_file_extension(file_path)
    assert file_extension == expected_extension


@pytest.mark.parametrize("file_name, expected_result", [
    ("file1.json", 'file1_parsed.json'),
    ("file2.json", 'file2_parsed.json')
])
def test_parse_file(file_name, expected_result):
    file_path = get_file_path(file_name)
    expected_result_path = get_file_path(expected_result)

    with open(expected_result_path, 'r') as expected_file:
        expected_data = json.load(expected_file)

    parsed_data = parse_file(file_path)
    assert parsed_data == expected_data
