        print("before", arr[i], arr[-i])
        arr[i], arr[-i] = arr[-i], arr[i]
        print("after", arr[i], arr[-i])