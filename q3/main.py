import unittest
import string
from collections import defaultdict


def solve1(inputs: list):
    summ = 0
    d = {c: i+1 for i, c in enumerate(string.ascii_lowercase)} | {
        c: i+27 for i, c in enumerate(string.ascii_uppercase)}
    for line in inputs:
        line.strip()
        l = len(line) // 2
        left, right = line[:l], line[l:]
        # only one element, use max() to get it
        common = max(set(left) & set(right))
        summ += d[common]
    print(summ)
    return summ


def solve2(inputs: list):
    summ = 0
    d = {c: i+1 for i, c in enumerate(string.ascii_lowercase)} | {
        c: i+27 for i, c in enumerate(string.ascii_uppercase)}
    for i in range(0, len(inputs), 3):
        left, middle, right = inputs[i], inputs[i+1], inputs[i+2]
        # only one element, use max() to get it
        common = max(set(left) & set(middle) & set(right))
        summ += d[common]
    print(summ)
    return summ


class TestStringMethods(unittest.TestCase):
    def test_solve_1(self):
        inputs = ["vJrwpWtwJgWrhcsFMMfFFhFp\n",
                  "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n",
                  "PmmdzqPrVvPwwTWBwg\n",
                  "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n",
                  "ttgJtRGJQctTZtZT\n",
                  "CrZsJsPPZsGzwwsLwLmpwMDw\n"]
        self.assertEqual(solve1(inputs), 157)

    def test_solve_real1(self):
        with open("./input.txt", "r") as f:
            inputs = [line for line in f.readlines()]
        solve1(inputs)

    def test_solve_2(self):
        inputs = ["vJrwpWtwJgWrhcsFMMfFFhFp\n",
                  "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n",
                  "PmmdzqPrVvPwwTWBwg\n",
                  "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n",
                  "ttgJtRGJQctTZtZT\n",
                  "CrZsJsPPZsGzwwsLwLmpwMDw\n"]
        self.assertEqual(solve2(inputs), 70)

    def test_solve_real2(self):
        with open("./input.txt", "r") as f:
            inputs = [line for line in f.readlines()]
        solve2(inputs)


if __name__ == '__main__':
    unittest.main(verbosity=0)
