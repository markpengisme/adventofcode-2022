import unittest
import string
from collections import defaultdict


def solve1(inputs: list):
    count = 0
    for line in inputs:
        first, second = line.strip().split(",")
        first_start, first_end = [int(i) for i in first.split("-")]
        second_start, second_end = [int(i) for i in second.split("-")]
        if first_start <= second_start and second_end <= first_end:
            count += 1
        elif second_start <= first_start and first_end <= second_end:
            count += 1
    print(count)
    return count


def solve2(inputs: list):
    count = 0
    for line in inputs:
        first, second = line.strip().split(",")
        first_start, first_end = [int(i) for i in first.split("-")]
        second_start, second_end = [int(i) for i in second.split("-")]
        if first_start <= second_start <= first_end or first_start <= second_end <= first_end or\
                second_start <= first_start <= second_end or second_start <= first_end <= second_end:
            count += 1
    print(count)
    return count


class TestStringMethods(unittest.TestCase):
    def test_solve_1(self):
        inputs = ["2-4,6-8",
                  "2-3,4-5",
                  "5-7,7-9",
                  "2-8,3-7",
                  "6-6,4-6",
                  "2-6,4-8"]
        self.assertEqual(solve1(inputs), 2)

    def test_solve_real1(self):
        with open("./input.txt", "r") as f:
            inputs = [line for line in f.readlines()]
        solve1(inputs)

    def test_solve_2(self):
        inputs = ["2-4,6-8",
                  "2-3,4-5",
                  "5-7,7-9",
                  "2-8,3-7",
                  "6-6,4-6",
                  "2-6,4-8"]
        self.assertEqual(solve2(inputs), 4)

    def test_solve_real2(self):
        with open("./input.txt", "r") as f:
            inputs = [line for line in f.readlines()]
        solve2(inputs)


if __name__ == '__main__':
    unittest.main(verbosity=0)
