with open('input.txt', 'r') as f:
    n, k = map(int, f.read().split(' '))

count = n ** 2 / k

if int(count) != count:
    print('No')
elif (k == 1) and (n > 1):
    print('No')
else:
    counts = [0] * k
    res = []

    for i in range(n):
        line = []
        for j in range(n):
            num = (i + j) % k
            counts[num] += 1
            line.append(str(num + 1))
        res.append(' '.join(line))

    if all(c == count for c in counts):
        print('Yes')
        print('\n'.join(res))
    else:
        print('No')
