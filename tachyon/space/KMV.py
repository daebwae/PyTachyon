__author__ = 'Stefan Zapf'
import hashlib
import sys


class KMV(object):
    def __init__(self, k):
        self._k_smallest = [float("inf") for x in range(k)]
        self._hash_size = hashlib.sha256().digest_size * 8

    def add(self, item):
        h = hashlib.sha256(item)
        n = int(h.hexdigest(), 16)
        if n in self._k_smallest:
            return

        max_val = max(self._k_smallest)
        max_idx = self._k_smallest.index(max_val)

        if n < max_val:
            self._k_smallest[max_idx] = n

    def compute(self):
        mean_dist = max(self._k_smallest) / float(len(self._k_smallest) - 1)
        return 2 ** self._hash_size / mean_dist


if __name__ == "__main__":
    kmv = KMV(5)
    for arg in sys.argv[1:]:
        kmv.add(arg)
    print kmv.compute
