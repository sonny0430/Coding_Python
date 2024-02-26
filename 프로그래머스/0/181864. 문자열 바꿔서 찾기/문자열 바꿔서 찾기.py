def solution(myString, pat):
    result = []
    for s in myString:
        if s == "A":
            result.append("B")
        elif s == "B":
            result.append("A")
    result = ''.join(result)
    return (1 if pat in result else 0)
