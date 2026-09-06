def num_obj(s):

    result = []

    for i in s:

        obj = {str(i): chr(i)}
        result.append(obj)

    return result


print(num_obj([118, 117, 120]))
