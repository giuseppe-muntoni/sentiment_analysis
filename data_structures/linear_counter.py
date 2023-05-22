from bitarray import bitarray

import math


class LinearCounter():
    def __init__(self, len):
        self.len = len
        self.mask = bitarray(len)
        self.mask.setall(0)

    def add(self, value):
        self.mask[hash(value) % len(self.mask)] = 1

    def count(self):
        return (-self.len) * math.log(
            (self.len - self.mask.count(1)) / self.len)

    def intersect(self, that):
        to_ret = LinearCounter(self.len)
        for i in range(0, len(self.mask)):
            to_ret.mask[i] = self.mask[i] and that.mask[i]
        return to_ret
