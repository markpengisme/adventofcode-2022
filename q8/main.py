import unittest


def check_four_dir(inputs, row, col):
    rows = len(inputs)
    cols = len(inputs[0])
    h = inputs[row][col]

    def check_top():
        for i in range(0, row):
            if inputs[i][col] >= h:
                return False
        return True

    def check_bottom():
        for i in range(row+1, rows):
            if inputs[i][col] >= h:
                return False
        return True

    def check_left():
        for i in range(0, col):
            if inputs[row][i] >= h:
                return False
        return True

    def check_right():
        for i in range(col+1, cols):
            if inputs[row][i] >= h:
                return False
        return True

    return check_top() or check_bottom() or check_left() or check_right()


def solve1(inputs: list):
    inputs = [[int(h) for h in row[:-1]] for row in inputs]
    rows = len(inputs)
    cols = len(inputs[0])
    count = 0
    for row in range(rows):
        for col in range(cols):
            if row == 0 or row == rows-1 or col == 0 or col == cols-1:
                count += 1
                continue
            count += 1 if check_four_dir(inputs, row, col) else 0
    print(count)
    return count


def get_scenic_score(inputs, row, col):
    rows = len(inputs)
    cols = len(inputs[0])
    h = inputs[row][col]

    def check_top():
        trees = 0
        for i in range(row-1, -1, -1):
            trees += 1
            if inputs[i][col] >= h:
                break
        return trees

    def check_bottom():
        trees = 0
        for i in range(row+1, rows):
            trees += 1
            if inputs[i][col] >= h:
                break
        return trees

    def check_left():
        trees = 0
        for i in range(col-1, -1, -1):
            trees += 1
            if inputs[row][i] >= h:
                break
        return trees

    def check_right():
        trees = 0
        for i in range(col+1, cols):
            trees += 1
            if inputs[row][i] >= h:
                break
        return trees

    return check_top() * check_bottom() * check_left() * check_right()


def solve2(inputs: list):
    inputs = [[int(h) for h in row[:-1]] for row in inputs]
    rows = len(inputs)
    cols = len(inputs[0])
    maxi = 0
    for row in range(rows):
        for col in range(cols):
            if row == 0 or row == rows-1 or col == 0 or col == cols-1:
                continue
            maxi = max(get_scenic_score(inputs, row, col), maxi)
    print(maxi)
    return maxi


class TestStringMethods(unittest.TestCase):
    def test_solve_1(self):
        inputs = [
            "30373\n",
            "25512\n",
            "65332\n",
            "33549\n",
            "35390\n",
        ]
        self.assertEqual(solve1(inputs), 21)

    def test_solve_real1(self):
        with open("./input.txt", "r") as f:
            inputs = [line for line in f.readlines()]
        solve1(inputs)

    def test_solve_2(self):
        inputs = [
            "30373\n",
            "25512\n",
            "65332\n",
            "33549\n",
            "35390\n",
        ]
        self.assertEqual(solve2(inputs), 8)

    def test_solve_real2(self):
        with open("./input.txt", "r") as f:
            inputs = [line for line in f.readlines()]
        solve2(inputs)


if __name__ == '__main__':
    unittest.main(verbosity=0)
