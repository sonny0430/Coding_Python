def solution(arr):
    tmp = max([len(arr), len(arr[0])])
    
    for i in range(tmp):
        if len(arr) < tmp:
            arr.append([0] * tmp)

    for i in range(tmp):
        while len(arr[i]) < tmp:
            arr[i].append(0)

    return arr
