def solution(a, b, c):
    temp = set([a,b,c])
    if len(temp) == 3:
        return a + b + c
    elif len(temp) == 2:
        return (a + b + c) * (a**2 + b**2 + c**2)
    elif len(temp) == 1:
        return (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)