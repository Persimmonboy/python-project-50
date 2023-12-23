def format_value(value, depth):
    if value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, dict):
        indent = '    ' * depth
        lines = [f'{indent}{key}: {format_value(val, depth + 1)}' for key, val in value.items()]
        return '{\n' + '\n'.join(lines) + '\n' + '    ' * (depth - 1) + '}'
    else:
        return str(value)


def format_stylish(diff, depth=1):
    indent = '    ' * (depth - 1)
    lines = []

    for key, value in diff.items():
        if isinstance(value, dict) and 'type' in value:
            if value['type'] == 'unchanged':
                lines.append(f'{indent}    {key}: {format_value(value["value"], depth + 1)}')
            elif value['type'] == 'added':
                lines.append(f'{indent}  + {key}: {format_value(value["value"], depth + 1)}')
            elif value['type'] == 'removed':
                lines.append(f'{indent}  - {key}: {format_value(value["value"], depth + 1)}')
            elif value['type'] == 'changed':
                lines.append(f'{indent}  - {key}: {format_value(value["old_value"], depth + 1)}')
                lines.append(f'{indent}  + {key}: {format_value(value["new_value"], depth + 1)}')
            elif value['type'] == 'nested':
                nested_indent = '    ' * depth
                lines.append(f'{nested_indent}{key}: {format_stylish(value["children"], depth + 1)}')
        else:
            lines.append(f'{indent}    {key}: {format_value(value, depth + 1)}')

    return '{\n' + '\n'.join(lines) + '\n' + indent + '}'
