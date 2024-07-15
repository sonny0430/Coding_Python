def solution(n):
    temp = []
    for s in str(n):
        temp.append(s)
    return int(''.join(sorted(temp, reverse=True)))