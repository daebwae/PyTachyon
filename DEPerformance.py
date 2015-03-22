__author__ = 'Stefan Zapf'

import sys
import random
import string
import pandas as pd
from ggplot import *

from tachyon.space import KMV

_available_algorithms = dict(kmv5=5, kmv10=10, kmv100=100)


def print_usage():
    print "Usage:"
    print "DEPerformance [algorithm] [steps] [step size] [repetitions]"
    print "Supported algorithms:"
    for algorithm in _available_algorithms.keys():
        print algorithm


def create_random_word(length):
    return ''.join([random.choice(string.ascii_letters) for x in range(length)])


def feed_algorithm(algorithm, word_count):
    selected_words = set()
    while len(selected_words) < word_count:

        word = create_random_word(random.randint(3, 15))
        for i in range(random.randint(1, 5)):
            algorithm.add(word)

        selected_words.add(word)


def visualize(algos, de, estimates):
    df = pd.DataFrame({
        "distinct elements": de,
        "estimate": estimates,
        "algorithm": algos,
        "upper": [x * 1.1 for x in de],
        "lower": [x * 0.9 for x in de]
    })
    print ggplot(df, aes(x='distinct elements', y='estimate')) \
          + geom_area(aes(fill='orange', color='orange', alpha='0.3', ymin='lower', ymax='upper')) \
          + geom_abline(colour='orange') + geom_point(color="skyblue", alpha=0.8, size=40)


def main(args):
    try:
        alg_param = _available_algorithms[args[0]]
        steps = int(args[1])
        step_size = int(args[2])
        repetitions = int(args[3])

        distinct_elements = []
        estimates = []
        algos = []

        for step in range(step_size, (steps + 1) * step_size, step_size):
            for rep in range(repetitions):
                print str(step) + ": " + str(rep + 1)
                algo = KMV.KMV(alg_param)
                feed_algorithm(algo, step)
                estimate = algo.compute()

                distinct_elements.append(step)
                estimates.append(estimate)
                algos.append("KMV")

    except Exception:
        print_usage()
        raise

    visualize(algos, distinct_elements, estimates)


if __name__ == "__main__":
    main(sys.argv[1:])

