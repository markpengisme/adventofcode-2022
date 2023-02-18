import unittest


class Node:
    def __init__(self, path, is_folder, size=0):
        self.path = path
        self.is_folder = is_folder
        self.size = size
        self.children = {}

    def __str__(self):
        children = [node.path for node in self.children.values()]
        return f"{self.path}, {self.is_folder}, {self.size}, {children}"


def buildTree(inputs):
    path = ["/"]
    root = curr = Node("/", True)
    link = {"/": root}
    for line in inputs:
        line = line.strip()
        if line[0] == "$":
            commands = line.split()
            if commands[1] == "cd":
                if commands[2] == "/":
                    path = ["/"]
                    curr = link["/"]
                elif commands[2] == ".." and path:
                    path.pop()
                    str_path = path[0] + "/".join(path[1:])
                    curr = link[str_path]
                else:
                    path.append(commands[2])
                    str_path = path[0] + "/".join(path[1:])
                    curr = link[str_path]
        else:
            size_or_folder, name = line.split()
            child_path = path[0] + "/".join(path[1:] + [name])
            if size_or_folder == "dir":
                child = Node(child_path, True)
                link[child_path] = child
                curr.children[child_path] = child
            else:
                child = Node(child_path, False, int(size_or_folder))
                link[child_path] = child
                curr.children[child_path] = child

    return root, link


def dfs(node: Node):
    if node.is_folder:
        size = 0
        for child in node.children.values():
            size += dfs(child)
        node.size = size
    return node.size


def solve1(inputs: list):
    root, link = buildTree(inputs)
    dfs(root)
    targets = []
    for node in link.values():
        # print(node)
        if node.is_folder and node.size <= 100000:
            targets.append(node)
    ans = sum([target.size for target in targets])
    print(ans)
    return ans


def solve2(inputs: list):
    root, link = buildTree(inputs)
    dfs(root)
    need = 70_000_000 - 30_000_000
    curr = root.size
    ans = float('inf')
    for node in link.values():
        if node.is_folder and curr - node.size <= need and node.size < ans:
            ans = node.size

    print(ans)
    return ans


class TestStringMethods(unittest.TestCase):
    def test_solve_1(self):
        inputs = [
            "$ cd /",
            "$ ls",
            "dir a",
            "14848514 b.txt",
            "8504156 c.dat",
            "dir d",
            "$ cd a",
            "$ ls",
            "dir e",
            "29116 f",
            "2557 g",
            "62596 h.lst",
            "$ cd e",
            "$ ls",
            "584 i",
            "$ cd ..",
            "$ cd ..",
            "$ cd d",
            "$ ls",
            "4060174 j",
            "8033020 d.log",
            "5626152 d.ext",
            "7214296 k"
        ]
        self.assertEqual(solve1(inputs), 95437)

    def test_solve_real1(self):
        with open("./input.txt", "r") as f:
            inputs = [line for line in f.readlines()]
        solve1(inputs)

    def test_solve_2(self):
        inputs = [
            "$ cd /",
            "$ ls",
            "dir a",
            "14848514 b.txt",
            "8504156 c.dat",
            "dir d",
            "$ cd a",
            "$ ls",
            "dir e",
            "29116 f",
            "2557 g",
            "62596 h.lst",
            "$ cd e",
            "$ ls",
            "584 i",
            "$ cd ..",
            "$ cd ..",
            "$ cd d",
            "$ ls",
            "4060174 j",
            "8033020 d.log",
            "5626152 d.ext",
            "7214296 k"
        ]
        self.assertEqual(solve2(inputs), 24933642)

    def test_solve_real2(self):
        with open("./input.txt", "r") as f:
            inputs = [line for line in f.readlines()]
        solve2(inputs)


if __name__ == '__main__':
    unittest.main(verbosity=0)
