import math


class AB(object):
    def createString(self, N, K):
        smaller_half = math.floor(N / 2)
        bigger_half = N - smaller_half
        if K > smaller_half * bigger_half:
            return ""
        return "WRONG"
