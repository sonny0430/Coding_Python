def solution(i, j, k):
    count = 0
    for s in range(i, j+1):
        if str(k) in str(s):
            count += str(s).count(str(k))
    return count