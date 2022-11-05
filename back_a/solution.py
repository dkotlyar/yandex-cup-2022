with open('input.txt', 'r') as f:
    file = f.readlines()
    N, M, _ = map(int, file[0].strip().split())
    events = map(lambda s: s.strip().split(), file[1:])

resets = [0] * N
state = [
    [1] * M
    for _ in range(N)
]

for event in events:
    if event[0] == 'DISABLE':
        n, m = map(int, event[1:])
        state[n - 1][m - 1] = 0
    elif event[0] == 'RESET':
        n = int(event[1]) - 1
        state[n] = [1] * M
        resets[n] += 1
    else:
        works = [
            sum(dc)
            for dc in state
        ]
        score = [
            work * reset_count
            for work, reset_count in zip(works, resets)
        ]
        if event[0] == 'GETMIN':
            print(score.index(min(score)) + 1)
        elif event[0] == 'GETMAX':
            print(score.index(max(score)) + 1)
