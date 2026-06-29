def arr_check(arr):

    for a in arr:

        if not isinstance(a, list):
            return False

    return True


print(arr_check([["string"]]))
print(arr_check([[], {}]))
