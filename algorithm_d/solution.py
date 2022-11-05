base = 'ACGT'

#   A C G T
# A 0 1 2 1
# C 1 0 1 2
# G 2 1 0 1
# T 1 2 1 0

dist = [
    [0, 1, 2, 1],
    [1, 0, 1, 2],
    [2, 1, 0, 1],
    [1, 2, 1, 0]
]

with open('input.txt', 'r') as f:
    file = f.readlines()
    nl = file[0].strip()
    N, L = map(int, nl.split())
    targets = list(map(lambda s: s.strip(), file[1:]))

exist_acids = [[0] * L]

targets_ids = [
    [
        base.index(_base)
        for _base in acid
    ]
    for acid in targets
]


steps = 0

while targets_ids:
    distances = [
        min([
            sum([
                dist[e_acid][t_acid]
                for t_acid, e_acid in zip(target, exist)
            ])
            for exist in exist_acids
        ])
        for target in targets_ids
    ]
    min_i = distances.index(min(distances))
    next = targets_ids.pop(min_i)
    exist_acids.append(next)
    steps += distances[min_i]

print(steps)

