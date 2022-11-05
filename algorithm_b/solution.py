with open('input.txt', 'r') as f:
    file = f.readlines()
    tasks = list(map(lambda s: list(map(int, s.strip().split(' '))), file[1:]))


def test_solution(num, b):
    while num > 0:
        if num % 10 % b:
            return 0
        num = num // 10
    return 1

[
    print(sum(
        test_solution(num, b)
        for num in range(1, n + 1)
    ))
    for n, b in tasks
]
