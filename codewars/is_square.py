def is_square(n):
    if n < 0:
        return False
    root = n**0.5
    if root == int(root):
        return True
    else:
        return False


print(is_square(3))
