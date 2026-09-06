def correct(s):

    return s.replace("0", "O").replace("1", "I").replace("5", "S")


print(correct("L0ND0N"))

# corrections = {'5': 'S', '0': 'O', '1': 'I'}
# return re.sub(r'[501]', lambda match: corrections[match.group(0)], text)
