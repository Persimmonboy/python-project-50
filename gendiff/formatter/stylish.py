def format_value(value, depth):
    if value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, dict):
        indent = '    ' * depth
        lines = [
            f'{indent}{key}: {format_value(val, depth + 1)}'
            for key, val in value.items()
        ]
        return '{\n' + '\n'.join(lines) + '\n' + '    ' * (depth - 1) + '}'
    else:
        return str(value)


def format_added(key, value, depth, indent):
    return f'{indent}  + {key}: {format_value(value["value"], depth + 1)}'


def format_removed(key, value, depth, indent):
    return f'{indent}  - {key}: {format_value(value["value"], depth + 1)}'


def format_changed(key, value, depth, indent):
    old_value = format_value(value["old_value"], depth + 1)
    new_value = format_value(value["new_value"], depth + 1)
    return f'{indent}  - {key}: {old_value}', f'{indent}  + {key}: {new_value}'


def format_nested(key, value, depth, indent):
    nested_indent = '    ' * depth
    nested_diff = format_stylish(value["children"], depth + 1)
    return f'{nested_indent}{key}: {nested_diff}'


def format_unchanged(key, value, depth, indent):
    return f'{indent}    {key}: {format_value(value["value"], depth + 1)}'


FORMATTERS = {
    'added': format_added,
    'removed': format_removed,
    'changed': format_changed,
    'nested': format_nested,
    'unchanged': format_unchanged,
}


def format_stylish(diff, depth=1):
    indent = '    ' * (depth - 1)
    lines = []

    for key, value in diff.items():
        if isinstance(value, dict) and 'type' in value:
            formatter = FORMATTERS[value['type']]
            result = formatter(key, value, depth, indent)
            if isinstance(result, tuple):
                lines.extend(result)
            else:
                lines.append(result)
        else:
            lines.append(
                f'{indent}    {key}: {format_value(value, depth + 1)}'
            )

    return '{\n' + '\n'.join(lines) + '\n' + indent + '}'
