import pytest
import os
from gendiff.generate_diff import generate_diff


FIXTURES_DIR = os.path.join('tests', 'fixtures')


def get_file_path(filename):
    return os.path.join(FIXTURES_DIR, filename)


@pytest.mark.parametrize("file1_name, file2_name, expected_result_name", [
    ("file1.json", "file2.json", "expected_result.txt")
])
def test_generator_diff(file1_name, file2_name, expected_result_name):
    file1_path = get_file_path(file1_name)
    file2_path = get_file_path(file2_name)
    expected_result_path = get_file_path(expected_result_name)

    with open(expected_result_path) as f:
        expected_result = f.read()

    generated_diff = generate_diff(file1_path, file2_path)
    assert generated_diff == expected_result