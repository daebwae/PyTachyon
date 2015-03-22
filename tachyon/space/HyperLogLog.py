from ..shared import BitBox
import sys

__author__ = 'Stefan Zapf'


class HyperLogLog(object):
    """ Implementation of HyperLogLog
    currently in dev, just a basic implementation
    """

    def __init__(self):
        self.max_zeroes = 0

    def add(self, item):
        h = hash(item)
        zeros = BitBox.CalcZeros(h)
        self.max_zeroes = max(self.max_zeroes, zeros)

    def compute(self):
        return 2 ** (self.max_zeroes + 1)


if __name__ == "__main__":
    hll = HyperLogLog()
    for arg in sys.argv[1:]:
        hll.add(arg)
    print hll.compute()
