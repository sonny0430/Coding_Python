def solution(myString, pat):
    a = pat.lower()
    b = myString.lower()
    if a in b:
        return 1
    else:
        return 0
    