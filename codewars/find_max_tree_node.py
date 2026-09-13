# binary tree
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def findMax(root):
    # Assume the current node is the biggest for now
    max_value = root.value

    # Check everything on the left
    if root.left is not None:
        left_max = findMax(root.left)

        if left_max > max_value:
            max_value = left_max

    # Check everything on the right
    if root.right is not None:
        right_max = findMax(root.right)

        if right_max > max_value:
            max_value = right_max

    return max_value