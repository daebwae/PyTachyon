__author__ = 'Stefan Zapf'
import hashlib
import sys


class KMV(object):
    def __init__(self, k):
        self._k = k
        self._kSmallest = [float("inf") for x in range(k)]

    def add(self, item):
        h = hashlib.md5(item)
        n = int(h.hexdigest(), 16)
        mv = max(self._kSmallest)
        mi = self._kSmallest.index(mv)

        if(n < mv):
            self._kSmallest[mi] = n

    def compute(self):
        mv_frac = max(self._kSmallest) / float(2**128)
        return (self._k - 1.) / mv_frac

if __name__ == "__main__":
    kmv = KMV(3)
    for arg in sys.argv[1:]:
        kmv.add(arg)
    print kmv.compute()
