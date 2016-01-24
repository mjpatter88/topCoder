from AB import AB


def test_create_string_2_1():
    N = 2
    K = 1
    ab = AB.AB()
    assert _count_pairs(ab.createString(N, K)) == 1, "N={} and K={}".format(N, K)


def test_create_string_all():
    ab = AB.AB()
    for N in range(2, 51):
        max_k = N * (N - 1) / 2
        for K in range(0, int(max_k + 1)):
            result = ab.createString(N, K)
            assert _count_pairs(result) == K, "N={} and K={}".format(N, K)


def _count_pairs(string):
    if len(string) < 2:
        return 0

    if string[0] == 'A':
        return string.count('B') + _count_pairs(string[1:])
    else:
        return _count_pairs(string[1:])