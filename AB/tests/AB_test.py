import math

from AB import AB


def test_create_string_2_1():
    N = 2
    K = 1
    ab = AB.AB()
    assert _count_pairs(ab.createString(N, K)) == 1, "N={} and K={}".format(N, K)


def _is_possible(N, K):
    smaller_half = math.floor(N / 2)
    bigger_half = N - smaller_half
    return K < smaller_half * bigger_half


def test_create_string_all():
    ab = AB.AB()
    test_results = {}
    for N in range(2, 51):
        max_k = N * (N - 1) / 2
        for K in range(0, int(max_k + 1)):
            result = ab.createString(N, K)
            test_results[(N, K)] = (_count_pairs(result) == K or (_count_pairs(result) == 0 and not _is_possible(N, K)))

    print("Total tests: {}".format(len(test_results)))
    print("Passed tests: {}".format(list(test_results.values()).count(True)))
    print("Failed tests: {}".format(list(test_results.values()).count(False)))


def _count_pairs(string):
    if len(string) < 2:
        return 0

    if string[0] == 'A':
        return string.count('B') + _count_pairs(string[1:])
    else:
        return _count_pairs(string[1:])


if __name__ == '__main__':
    test_create_string_all()
