def get_nested(boxes, parent=None):
    # print(f'{boxes=}')
    nested = []
    for n, box in boxes:
        box_ = sorted(box)
        if not parent or all(p > b for b, p in zip(box_, parent)):
            _nested = get_nested(boxes[:n] + boxes[n+1:], box_)
            _nested.append(n)
            if len(_nested) > len(nested):
                nested = _nested

    return nested


with open(f'input.txt', 'r') as f:
    input_txt = f.readlines()
    boxes = list(map(lambda s: list(map(int, s.split())), input_txt[1:]))

rest_boxes = list(enumerate(boxes))
nested = get_nested(rest_boxes)

print(len(nested))
print(*map(lambda n: n + 1, nested))
