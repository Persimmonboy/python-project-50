from gendiff.parser import parse_file


def convert_bool_to_string(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def handle_added(key, value2):
    return {'type': 'added', 'value': convert_bool_to_string(value2)}


def handle_removed(key, value1):
    return {'type': 'removed', 'value': convert_bool_to_string(value1)}


def handle_changed(key, value1, value2):
    return {
        'type': 'changed',
        'old_value': convert_bool_to_string(value1),
        'new_value': convert_bool_to_string(value2)
    }


def handle_nested(key, value1, value2, build_diff_func):
    return {
        'type': 'nested',
        'children': build_diff_func(value1, value2)
    }


def handle_unchanged(key, value1):
    return {'type': 'unchanged', 'value': convert_bool_to_string(value1)}


def determine_change(key, value1, value2, data1, data2, build_diff_func):
    if key in data1 and key not in data2:
        return handle_removed(key, value1)
    elif key not in data1 and key in data2:
        return handle_added(key, value2)
    elif isinstance(value1, dict) and isinstance(value2, dict):
        return handle_nested(key, value1, value2, build_diff_func)
    elif value1 == value2:
        return handle_unchanged(key, value1)
    else:
        return handle_changed(key, value1, value2)


def generate_diff(file1, file2):
    file1_data = parse_file(file1)
    file2_data = parse_file(file2)

    def build_diff(data1, data2):
        keys = sorted(data1.keys() | data2.keys())
        diff = {}

        for key in keys:
            value1 = data1.get(key)
            value2 = data2.get(key)
            diff[key] = determine_change(
                key, value1, value2, data1, data2, build_diff
            )

        return diff

    return build_diff(file1_data, file2_data)
