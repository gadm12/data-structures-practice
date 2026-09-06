def switch_dict(dic):
    results = {}

    for k, v in dic.items():

        if v not in results:
            results[v] = [k]

        else:

            results[v].append(k)
    return results


print(switch_dict({"Ice": "Cream", "Age": "21", "Light": "Cream", "Double": "Cream"}))
