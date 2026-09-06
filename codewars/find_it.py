# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring


def find_it(seq):

    counter = {}

    for n in seq:
        counter[n] = counter.get(n, 0) + 1

    for k, v in counter.items():
        if v % 2 != 0:
            return k
    print("not found")
