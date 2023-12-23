def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'" if value not in ['true', 'false', 'null'] else value
    else:
        return str(value)

def format_plain(diff, parent=''):
    lines = []
    for key, value in sorted(diff.items()):
        path = f"{parent}.{key}" if parent else key
        if value['type'] == 'nested':
            lines.append(format_plain(value['children'], path))
        elif value['type'] == 'added':
            added_value = format_value(value['value'])
            lines.append(f"Property '{path}' was added with value: {added_value}")
        elif value['type'] == 'removed':
            lines.append(f"Property '{path}' was removed")
        elif value['type'] == 'changed':
            old_value = format_value(value['old_value'])
            new_value = format_value(value['new_value'])
            lines.append(f"Property '{path}' was updated. From {old_value} to {new_value}")
    return '\n'.join(lines)
