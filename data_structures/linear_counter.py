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

    def count_intersection(self, that):
        union_lc = LinearCounter(self.len)
        for i in range(0, len(self.mask)):
            union_lc.mask[i] = self.mask[i] or that.mask[i]
        return (self.count() + that.count() - union_lc.count())
    
    def count_union(self, that):
        union_lc = LinearCounter(self.len)
        for i in range(0, len(self.mask)):
            union_lc.mask[i] = self.mask[i] or that.mask[i]
        return union_lc.count()
