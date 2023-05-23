from bitarray import bitarray
from data_structures.hash_family import hash_n


class BloomFilter():
    def __init__(self, len, k=1):
        self.hashes = [hash_n(i) for i in range(k)]
        self.len = len
        self.mask = bitarray(len)
        self.mask.setall(0)

    def add(self, value):
        for hash in self.hashes:
            self.mask[hash(value) % len(self.mask)] = 1

    def contains(self, value):
        for hash in self.hashes:
            if self.mask[hash(value) % len(self.mask)] == 0:
                return False
        return True
