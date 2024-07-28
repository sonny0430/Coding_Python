def solution(x):
    temp = [int(s) for s in str(x)]
    return (True if x%sum(temp) == 0 else False)
