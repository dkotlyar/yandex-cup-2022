import operator
from functools import reduce
from itertools import combinations, chain, islice

with open('input.txt', 'r') as f:
    n = int(f.readline())
    poises = list(map(int, f.readline().split()))


def test(poises_set, n):
    all_combinations = [
        combinations(poises_set, k)
        for k in range(1, len(poises_set) + 1)
    ]
    all_combinations = reduce(operator.iconcat, all_combinations, [])
    all_combinations = list(map(set, all_combinations))

    bowl_sum = [
        abs(sum(left) - sum(right))
        for left, right in chain(
            (
                (
                    left, []
                )
                for left in all_combinations
            ),
            (
                (
                    left, right
                )
                for left, right in combinations(all_combinations, 2)
                if not left.intersection(right)
            )
        )
    ]

    return all([m in bowl_sum for m in range(1, n + 1)])


if sum(poises) < n:
    print('No')
else:
    if test(poises[:-10], n):
        print('Yes')
    elif test(poises[:10], n):
        print('Yes')
    else:
        print('No')

