def solution(arr):
    result =[]
    temp = []
    if arr.count(2) > 1:
        for i in range(len(arr)):
            if arr[i] == 2:
                temp.append(i)
        result = arr[temp[0]:temp[-1]+1]
        return result
    
    elif arr.count(2) == 1:
        return [2]
    else:
        return [-1]