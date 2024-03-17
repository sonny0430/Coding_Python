def solution(arr):
    for i in range(0, 11):
        if len(arr) == (2**i):
            return arr
        elif len(arr) < (2**(i)):
            for j in range(((2**(i)) - len(arr))):
                arr.append(0)
            break
    return arr   