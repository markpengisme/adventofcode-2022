import unittest
from collections import defaultdict


def solve(inputs: list):
    data = defaultdict(int)
    i = 0
    for line in inputs:
        if line == "\n":
            i += 1
        else:
            data[i] += int(line.strip())
    elves = sorted(data.values(), reverse=True)
    ans1 = elves[0]
    ans2 = sum(elves[:3])
    print(ans1, ans2)
    return ans1, ans2


class TestStringMethods(unittest.TestCase):
    def test_solve_1(self):
        inputs = ['1', '\n',
                  '2', '3', '\n',
                  '4', '\n',
                  '0', '\n',
                  '6', '\n',
                  '2']
        self.assertEqual(solve(inputs), (6, 15))

    def test_solve_real(self):
        with open("./input.txt", "r") as f:
            inputs = [line for line in f.readlines()]
        solve(inputs)


if __name__ == '__main__':
    unittest.main(verbosity=0)
