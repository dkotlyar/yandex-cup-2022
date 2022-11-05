import re
from math import copysign

alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_all = alphabet + '+-='

with open('input.txt', 'r') as f:
    for phrase in f.readlines():
        phrase = ''.join(c for c in phrase.strip() if c in alphabet_all)

        min_base = max([
            alphabet.index(c) if c in alphabet else -1
            for c in phrase
        ]) + 1
        max_base = 36

        def get_value(phrase, base):
            result = 0
            sign = 1
            for part in re.split(r'([+-])', phrase):
                if part in ['+', '-']:
                    sign = [-1, 1][part == '+']
                else:
                    value = int(part, base)
                    result += copysign(value, sign)
            return result


        left_part, right_part = phrase.split('=')
        for base in range(min_base, max_base + 1):
            left_ = get_value(left_part, base)
            right_ = get_value(right_part, base)
            if left_ == right_:
                print(base)
                break
        else:
            print(-1)

