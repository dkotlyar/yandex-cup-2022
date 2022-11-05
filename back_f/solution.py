import time

with open('input.txt', 'r') as f:
    input_txt = f.readlines()
    n, ZEROS, ONES, OPERATIONS = map(int, input_txt[0].strip().split())
    hashes = list(map(lambda s: s.strip(), input_txt[1:n + 1]))


def do(s, k):
    a, b, c = map(int, s[k - 1: k + 2])
    d = a ^ b ^ c
    s = s[:k] + str(d) + s[k+1:]
    return s


def do2(s, op, tl=1.):
    t = time.time()
    for k in range(1, len(s) - 2):
        if time.time() - t > tl:
            return None

        if op == 1:
            new_s = do(s, k)
            ones = len([bit for bit in new_s if bit == '1'])
            zeros = len(new_s) - ones
            if ones == ONES and zeros == ZEROS:
                return new_s, [k]
        else:
            answer = do2(do(s, k), op - 1, tl=tl - (time.time() - t))
            if answer:
                new_s, ops = answer
                ops = [k] + ops
                return new_s, ops


for hash in hashes:
    answer = do2(hash, OPERATIONS, tl=10 / len(hashes))

    if answer:
        new_s, ops = answer
        print(new_s)
        print(*[op + 1 for op in ops], sep=' ')
    else:
        print(-1)
