import unittest
import string
from collections import Counter


def solve1(inputs: list, width):
    ans = []
    for line in inputs:
        line += "#"
        counter = Counter(line[:width])
        for i in range(width, len(line)):
            if len(counter.keys()) == width:
                ans.append(i)
                break
            counter[line[i]] += 1
            counter[line[i-width]] -= 1
            if counter[line[i-width]] == 0:
                del counter[line[i-width]]
    print(ans)
    return ans


class TestStringMethods(unittest.TestCase):
    def test_solve_1(self):
        inputs = [
            "bvwbjplbgvbhsrlpgdmjqwftvncz",
            "nppdvjthqldpwncqszvftbrmjlhg",
            "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
            "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
        ]
        self.assertListEqual(solve1(inputs, 4), [5, 6, 10, 11])

    def test_solve_real1(self):
        with open("./input.txt", "r") as f:
            inputs = [line for line in f.readlines()]
        solve1(inputs, 4)

    def test_solve_2(self):
        inputs = [
            "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
            "bvwbjplbgvbhsrlpgdmjqwftvncz",
            "nppdvjthqldpwncqszvftbrmjlhg",
            "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
            "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
        ]
        self.assertListEqual(solve1(inputs, 14), [19, 23, 23, 29, 26])

    def test_solve_real2(self):
        with open("./input.txt", "r") as f:
            inputs = [line for line in f.readlines()]
        solve1(inputs, 14)


if __name__ == '__main__':
    unittest.main(verbosity=0)
