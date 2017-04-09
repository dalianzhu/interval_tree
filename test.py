from interval_tree import Node, IntervalTree

def test_case_1():
    tree = IntervalTree(1, 10)
    tree.insert_line(2, 6)

    print(tree.search_line(2, 7))
    print(tree.search_line(3, 5))

    print("over")

cases = [
    test_case_1,
]

for item in cases:
    item()