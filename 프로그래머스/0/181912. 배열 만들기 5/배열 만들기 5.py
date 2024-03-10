def solution(intStrs, k, s, l):
    result = []
    for i in range(len(intStrs)):
        if int(intStrs[i][s:s+l]) > k:
            result.append(int(intStrs[i][s:s+l]))
    return result