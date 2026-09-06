def problem(a):
    
    if isinstance(a,(int,float)):
        return (a*50)+6
    else:
        return "Error"


print(problem("hello"))

print(problem(1))
