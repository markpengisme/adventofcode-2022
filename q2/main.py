import unittest
from collections import defaultdict


def solve1(inputs: list):
    def pk(op, mine):
        summ = 0
        mine = ord(mine)
        summ += mine - ord('W')
        mine = chr(mine - 23)
        if op == mine:
            summ += 3
        elif op + mine in ["AB", "BC", "CA"]:
            summ += 6
        # print(summ, op, mine)
        return summ

    scores = 0
    for line in inputs:
        scores += pk(line[0], line[2])
    print(scores)
    return scores


def solve2(inputs: list):
    # X=0, Y=3, Z=6
    # A=1, B=2, C=3
    score_map = {
        "AX": 3, "AY": 4, "AZ": 8,
        "BX": 1, "BY": 5, "BZ": 9,
        "CX": 2, "CY": 6, "CZ": 7,
    }

    scores = 0
    for line in inputs:
        scores += score_map[line[0]+line[2]]
    print(scores)
    return scores


class TestStringMethods(unittest.TestCase):
    def test_solve_1(self):
        inputs = ["A Y\n",
                  "B X\n",
                  "C Z\n"]
        self.assertEqual(solve1(inputs), 15)

    def test_solve_real1(self):
        with open("./input.txt", "r") as f:
            inputs = [line for line in f.readlines()]
        solve1(inputs)

    def test_solve_2(self):
        inputs = ["A Y\n",
                  "B X\n",
                  "C Z\n"]
        self.assertEqual(solve2(inputs), 12)

    def test_solve_real2(self):
        with open("./input.txt", "r") as f:
            inputs = [line for line in f.readlines()]
        solve2(inputs)


if __name__ == '__main__':
    unittest.main(verbosity=0)
