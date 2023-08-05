import os
import json
import yaml

def get_file_extension(filepath):
    base_name, extension = os.path.splitext(filepath)
    return extension[1:]

def read_file_content(filepath):
    with open(filepath, 'r') as file:
        content = file.read()
    return content

def parse_file(filepath):
    extension = get_file_extension(filepath)
    content = read_file_content(filepath)

    if extension == 'json':
        return json.loads(content)
    elif extension in ['yml', 'yaml']:
        return yaml.safe_load(content)
    else:
        raise ValueError("Неподдерживаемое расширение файла")
