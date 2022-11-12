import json

with open('input.txt', 'r') as f:
    input_txt = f.readlines()
    json_data = json.loads(input_txt[0])

    requests = map(lambda s: json.loads(s), input_txt[2:])


def handle_node(node, key=None):
    pathes = []
    values = []

    if not isinstance(node, dict):
        return [key], [node]

    for k, _node in node.items():
        _pathes, _values = handle_node(_node, key=k)
        if key:
            _pathes = [f'{key}.{path}' for path in _pathes]

        pathes.extend(_pathes)
        values.extend(_values)

    return pathes, values


pathes, values = handle_node(json_data)

for req in requests:
    path, count = req['path'], req['count']
    left_path, right_path = path.split('*')
    L = [
        (value, type(value))
        for path, value in zip(pathes, values)
        if (
                path.startswith(left_path) and
                path.endswith(right_path) and
                len(path) > len(left_path) + len(right_path) and
                value
        )
    ]
    if len(L) == 0:
        result = []
    else:
        is_str = L[0][1] == str
        if all(not ((_type == str) ^ is_str) for value, _type in L):
            result = sorted([value for value, _ in L], reverse=True)[:count]
        else:
            result = None

    print(json.dumps(dict(result=result)))
