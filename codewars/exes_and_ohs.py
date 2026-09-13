def xo(s):
    exes = []
    ohs = []
    for l in s.lower():
        if l == "x":
            exes.append(l)
        elif l == "o":
            ohs.append(l)
    return len(exes) == len(ohs)



print(xo("ooxx"))
print(xo("zpzp"))
print(xo("zzOo"))
