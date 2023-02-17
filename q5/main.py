import unittest
import string
from collections import defaultdict


def solve1(inputs: list):
    data, ops = [], []
    to = data
    for line in inputs:
        if line == "\n":
            to = ops
            continue
        to.append(line.strip("\n"))

    data.pop()
    d = defaultdict(list)
    for row in data[::-1]:
        for i in range(1, len(row), 4):
            if row[i] != ' ':
                d[i//4+1].append(row[i])

    for op in ops:
        op = op.split(" ")
        amount, f, t = int(op[1]), int(op[3]), int(op[5])
        for _ in range(amount):
            d[t].append(d[f].pop())
    ans = "".join([arr[-1] for arr in d.values()])
    print(ans)
    return ans


def solve2(inputs: list):
    data, ops = [], []
    to = data
    for line in inputs:
        if line == "\n":
            to = ops
            continue
        to.append(line.strip("\n"))

    data.pop()
    d = defaultdict(list)
    for row in data[::-1]:
        for i in range(1, len(row), 4):
            if row[i] != ' ':
                d[i//4+1].append(row[i])

    for op in ops:
        op = op.split(" ")
        amount, f, t = int(op[1]), int(op[3]), int(op[5])
        d[t] += d[f][-amount:]
        d[f] = d[f][:-amount]

    ans = "".join([arr[-1] for arr in d.values()])
    print(ans)
    return ans


class TestStringMethods(unittest.TestCase):
    def test_solve_1(self):
        inputs = [
            "    [D]    \n",
            "[N] [C]    \n",
            "[Z] [M] [P]\n",
            " 1   2   3 \n",
            "\n",
            "move 1 from 2 to 1\n",
            "move 3 from 1 to 3\n",
            "move 2 from 2 to 1\n",
            "move 1 from 1 to 2\n",
        ]
        self.assertEqual(solve1(inputs), "CMZ")

    def test_solve_real1(self):
        with open("./input.txt", "r") as f:
            inputs = [line for line in f.readlines()]
        solve1(inputs)

    def test_solve_2(self):
        inputs = [
            "    [D]    \n",
            "[N] [C]    \n",
            "[Z] [M] [P]\n",
            " 1   2   3 \n",
            "\n",
            "move 1 from 2 to 1\n",
            "move 3 from 1 to 3\n",
            "move 2 from 2 to 1\n",
            "move 1 from 1 to 2\n",
        ]
        self.assertEqual(solve2(inputs), "MCD")

    def test_solve_real2(self):
        with open("./input.txt", "r") as f:
            inputs = [line for line in f.readlines()]
        solve2(inputs)


if __name__ == '__main__':
    unittest.main(verbosity=0)
