import math


class AB(object):
    def createString(self, N, K):
        letters = ""
        smaller_half = math.floor(N / 2)
        bigger_half = N - smaller_half
        if K > smaller_half * bigger_half:
            return letters

        remainder = K
        letters = ["B"] * N
        index = 0
        while remainder > 0 and index < N:
            new_pairs = N - 1 - index
            lost_pairs = letters.count("A")
            increase = new_pairs - lost_pairs
            if remainder >= increase:
                letters[index] = "A"
                remainder -= increase
            index += 1

        return "".join(letters)
