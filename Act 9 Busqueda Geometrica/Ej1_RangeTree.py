import random

class RangeTree:
    def __init__(self, points):
        self.root = self.build_range_tree(points)

    class Node:
        def __init__(self, point):
            self.point = point
            self.left = None
            self.right = None

    def build_range_tree(self, points):
        if not points:
            return None

        points.sort()
        mid = len(points) // 2
        root = self.Node(points[mid])

        left_points = points[:mid]
        right_points = points[mid + 1:]

        root.left = self.build_range_tree(left_points)
        root.right = self.build_range_tree(right_points)

        return root

    def range_query(self, x1, x2):
        result = []
        self.query_range_tree(self.root, x1, x2, result)
        return result

    def query_range_tree(self, node, x1, x2, result):
        if node is None:
            return

        if x1 <= node.point <= x2:
            result.append(node.point)

        if x1 <= node.point:
            self.query_range_tree(node.left, x1, x2, result)

        if node.point <= x2:
            self.query_range_tree(node.right, x1, x2, result)

if __name__ == "__main__":
    random_points = [random.uniform(-10, 10) for _ in range(2000)]
    range_tree = RangeTree(random_points)
    
    x1 = 9
    x2 = 9.5
    result = range_tree.range_query(x1, x2)
    print(f"Points in the range [{x1}, {x2}]: {result}")

