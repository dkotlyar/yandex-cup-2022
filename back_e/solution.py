from collections import Counter

with open('input.txt', 'r') as f:
    input_txt = f.readlines()
    _index = 0
    _count = int(input_txt[_index])
    black_list = list(map(lambda s: s.strip(), input_txt[_index + 1:_index + _count + 1]))
    _index = _index + _count + 1
    _count = int(input_txt[_index])
    file_list = list(map(lambda s: s.strip(), input_txt[_index + 1:_index + _count + 1]))
    _index = _index + _count + 1
    _count = int(input_txt[_index])
    req_list = list(map(lambda s: s.strip(), input_txt[_index + 1:_index + _count + 1]))

file_list = [
    (
        file, sum([
            1 if file.startswith(bl) else 0
            for bl in black_list
        ]) > 0
    )
    for file in file_list
]

for req in req_list:
    filtered_files = [
        (file, flag)
        for file, flag in file_list
        if file.startswith(req)
    ]
    deleted_files = [
        file
        for file, flag in filtered_files
        if flag
    ]
    deleted_extensions = [
        file.split('.')[1]
        for file in deleted_files
    ]
    counter = Counter(deleted_extensions)
    print(len(counter))
    for k, v in counter.items():
        print(f'.{k}: {v}')