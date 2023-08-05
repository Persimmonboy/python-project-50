from gendiff.parser import parse_file

def convert_bool_to_string(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value

def generate_diff(file1, file2):
    file1_data = parse_file(file1)
    file2_data = parse_file(file2)

    def build_diff(data1, data2):
        keys = sorted(data1.keys() | data2.keys())
        diff = {}

        for key in keys:
            # Получаем значения для ключа в обоих файлах
            value1 = data1.get(key)
            value2 = data2.get(key)

            # Конвертируем булевы значения в строки
            value1 = convert_bool_to_string(value1)
            value2 = convert_bool_to_string(value2)

            if key in data1 and key not in data2:
                diff[key] = {'type': 'removed', 'value': value1}
            elif key not in data1 and key in data2:
                diff[key] = {'type': 'added', 'value': value2}
            elif isinstance(value1, dict) and isinstance(value2, dict):
                diff[key] = {'type': 'nested', 'children': build_diff(value1, value2)}
            elif value1 == value2:
                diff[key] = {'type': 'unchanged', 'value': value1}
            else:
                diff[key] = {'type': 'changed', 'old_value': value1, 'new_value': value2}

        return diff

    return build_diff(file1_data, file2_data)
